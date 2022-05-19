import numpy as np
from scipy.optimize import curve_fit
import cv2

from variables import *

def stream_image(stream_queue, return_queue):
    while True:
        if not stream_queue.empty():
            element = stream_queue.get()
            if str(type(element[0])) == "<class 'str'>":
                if element[0] == 'EXIT': break
            image = element[0]
            para = element[1]

            if image is None: continue

            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            nypixel, nxpixel = image.shape
            ratio = [nxpixel/para.stream_size[0], nypixel/para.stream_size[1]]

            xmin = -round(nxpixel/2)
            ymin = -round(nypixel/2)

            xinterval = 1 / para.pixel_per_mm[0]
            yinterval = 1 / para.pixel_per_mm[1]

            xbin = [xmin + float(i) * xinterval for i in range(nxpixel)]
            ybin = [ymin + float(i) * yinterval for i in range(nypixel)]

            if para.intensity_line[0] == -1: para.intensity_line[0] = round(para.stream_size[0]/2)
            if para.intensity_line[1] == -1: para.intensity_line[1] = round(para.stream_size[1]/2)

            actual_line = [round(para.intensity_line[0]*ratio[0]), round(para.intensity_line[1]*ratio[1])]

            yhist, xhist = image[:,actual_line[0]], image[actual_line[1],:]

            return_queue.put([STREAM, image, xbin, ybin, xhist, yhist])

def analyze_image(analyze_queue, return_queue):
    while True:
        if not analyze_queue.empty():
            element = analyze_queue.get()
            if str(type(element[0])) == "<class 'str'>":
                if element[0] == 'EXIT': break
            image = element[0]

            if image is None: continue
            para = element[1]

            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.flip(image, 0)

            nypixel, nxpixel = image.shape

            xhist, yhist = [], []

            xhist = [0 for i in range(nxpixel)]
            yhist = [0 for i in range(nypixel)]
        
            for xidx in range(nxpixel):
                for yidx in range(nypixel):
                    xhist[xidx] += image[yidx][xidx] / 255
                    yhist[yidx] += image[yidx][xidx] / 255

            # 1. Calculate the center of mass in pixel space
            # Function spends more time when the reference point is the image array's zero.
            # The image center as the reference point shows better performance.
            image_center = np.array([round(nxpixel/2), round(nypixel/2)])

            numerator = np.array([0,0], dtype='int64') # x, y
            denominator = 0
            for iypixel in range(nypixel):
                for ixpixel in range(nxpixel):
                    intensity = image[iypixel][ixpixel]
                    distance =  np.array([ixpixel, iypixel]) - image_center
                    
                    numerator = numerator + intensity * distance
                    denominator += intensity

            center_pixel = numerator/denominator + image_center # beam center
            center_pixel = np.array([int(round(center_pixel[0])), int(round(center_pixel[1]))])

            # 2. Convert pixel space to real space
            # First, getting mapping between real coordinate and pixel coordinate
            # Second, find real space zero
            # Third, convert pixel beam center to real
            p1, p2, p3, p4 = para.cal_dest_points.values()
            p1 = np.array(p1)

            if para.calibrated:
                coordinate_center = np.array(p1[0]) - np.array(abs(p1[1])) / np.array(para.pixel_per_mm) # pixel
            else:
                coordinate_center = image_center # pixel

            para.coordinate_center = coordinate_center
            center_real = (center_pixel - coordinate_center) / np.array(para.pixel_per_mm) # mm

            xminimum = -coordinate_center[0]/para.pixel_per_mm[0] # mm
            yminimum = -coordinate_center[1]/para.pixel_per_mm[1] # mm

            xbin = [xminimum + float(i)/para.pixel_per_mm[0] for i in range(nxpixel)]
            xbin.sort()

            ybin = [yminimum + float(i)/para.pixel_per_mm[1] for i in range(nypixel)]
            ybin.sort()
            gauss = lambda x, a, b, c: a*np.exp(-2*(x-b)**2/c**2)
            try:
                xfitpara, xfitconv = curve_fit(gauss, xbin, xhist)
                xfitvalue = gauss(xbin, *xfitpara)
                try:
                    xwidth = 2*xfitpara[2]
                    xerror = 2*np.absolute(xfitconv[2][2]**0.5)
                except:
                    xwidth = 0.0
                    xerror = 0.0
            except:
                xfitvalue = [0 for i in range(len(xbin))]
                xwidth = len(np.where(xhist > 0.135*max(xhist))[0])
                xerror = 0.0
            try:
                yfitpara, yfitconv = curve_fit(gauss, ybin, yhist)
                yfitvalue = gauss(ybin, *yfitpara)
                try:
                    ywidth = 2*yfitpara[2]
                    yerror = 2*np.absolute(yfitconv[2][2]**0.5)
                except:
                    ywidth = 0.0
                    yerror = 0.0
            except:
                yfitvalue = [0 for i in range(len(ybin))]
                ywidth = len(np.where(yhist > 0.135*max(yhist))[0])
                yerror = 0.0

            image = cv2.flip(image, 0)
            return_element = [ANALYSIS, para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue,
                center_pixel, center_real, [xwidth, xerror], [ywidth, yerror]]

            from DigiMon import mutex

            mutex.acquire()
            while not return_queue.empty():
                return_queue.get()
            return_queue.put(return_element)
            mutex.release()