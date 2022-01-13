import numpy as np
from scipy.optimize import curve_fit
import cv2

from variables import *

def rotate_image(image, angle, quadrant = 0, flip_rl = 0, flip_ud = 0):
    center = (round(image.shape[1]/2), round(image.shape[0]/2))
    angle = float(angle)

    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    image = cv2.warpAffine(image, matrix, (0,0))

    if quadrant == 90:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif quadrant == 180:
        image = cv2.rotate(image, cv2.ROTATE_180)
    elif quadrant == 270:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    if flip_rl == 1:
        image = cv2.flip(image, 1)
    
    if flip_ud == 1:
        image = cv2.flip(image, 0)

    return image

def filter_image(image, filter_code, filter_para):
    if filter_code == BKG_SUBSTRACTION:
        background = cv2.imread(filter_para['background file'])
        image = cv2.subtract(image, background)
    if filter_code == GAUSSIAN_FILTER:
        ksize = (filter_para['x kernal size'], filter_para['y kernal size'])
        sigmaX = filter_para['sigmaX']
        image = cv2.GaussianBlur(image, ksize=ksize, sigmaX=sigmaX)
    elif filter_code == MEDIAN_FILTER:
        ksize = filter_para['kernal size']
        image = cv2.medianBlur(image, ksize=ksize)
    elif filter_code == BILATERAL_FILTER:
        ksize = filter_para['kernal size']
        scolor = filter_para['sigma color']
        sspace = filter_para['sigma space']
        image = cv2.bilateralFilter(image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
    else:
        image = image
    
    return image

def transform_image(image, transform_points, destination_points):
    #destination_points = [(0,0),(0,height),(width,0),(width,height)]
    transform_matrix = cv2.getPerspectiveTransform(np.float32(transform_points), np.float32(destination_points))

    width, height = image.shape[1], image.shape[0]
    image = cv2.warpPerspective(image, transform_matrix, (width, height))
    
    return image

def slice_image(image, ROI):
    if ROI == [[0,0],[0,0]] or [ROI[1][0], ROI[1][1]] == [image.shape[1], image.shape[0]]: return image

    x, y, width, height = ROI[0][0], ROI[0][1], ROI[1][0], ROI[1][1]
    src = image.copy()
    image = src[y:y+height, x:x+width]

    return image

def analyze_image(queue_for_analyze, return_queue):
    while True:
        if not queue_for_analyze.empty():
            element = queue_for_analyze.get()

            image = element[0]
            intensity_line = element[1]
            pixel_per_mm = element[2]
            original_pixel = element[3]
            resized_pixel = element[4]
            shot = element[5]

            if len(image.shape) == 3:
                grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else:
                grayimage = image

            nypixel, nxpixel = grayimage.shape

            total_x = nxpixel / pixel_per_mm[0]
            total_y = nypixel / pixel_per_mm[1]
            xmin = -round(total_x / 2.0)
            ymin = -round(total_y / 2.0)

            if not shot:
                grayimage = cv2.resize(grayimage, dsize=(resized_pixel[0], resized_pixel[1]), interpolation=cv2.INTER_LINEAR)
            
            nypixel, nxpixel = grayimage.shape
            if shot:
                xbin = [xmin + float(i) * (1.0/pixel_per_mm[0]) for i in range(nxpixel)]
                ybin = [ymin + float(i) * (1.0/pixel_per_mm[1]) for i in range(nypixel)]
            else:
                xinterval = abs(xmin) * 2 / nxpixel
                yinterval = abs(ymin) * 2 / nypixel
                
                xbin = [xmin + xinterval * float(i) for i in range(nxpixel)]
                ybin = [ymin + yinterval * float(i) for i in range(nypixel)]

            xhist, yhist = [], []
            if shot:
                xhist = [0 for i in range(nxpixel)]
                yhist = [0 for i in range(nypixel)]
            
                for xidx in range(nxpixel):
                    for yidx in range(nypixel):
                        xhist[xidx] += grayimage[yidx][xidx]
                        yhist[yidx] += grayimage[yidx][xidx]
            else:
                if intensity_line[0] == -1: intensity_line[0] = round(nxpixel / 2) - 1
                if intensity_line[1] == -1: intensity_line[1] = round(nypixel / 2) - 1
                
                yhist, xhist = grayimage[:,intensity_line[0]], grayimage[intensity_line[1],:]

            max_intensity = np.amax(grayimage)
            if max_intensity > 0:
                xhist_percent = np.asarray(xhist)/max_intensity * 100
                yhist_percent = np.asarray(yhist)/max_intensity * 100
            else:
                xhist_percent = np.asarray(xhist)*0
                yhist_percent = np.asarray(yhist)*0

            xmax, ymax = np.argmax(xhist_percent), np.argmax(yhist_percent)

            xlength = len(np.where(xhist_percent > 32)[0]) / pixel_per_mm[0]
            ylength = len(np.where(yhist_percent > 32)[0]) / pixel_per_mm[1]
            
            return_element = [grayimage, xbin, ybin, xhist_percent, yhist_percent, [xbin[xmax], xlength], [ybin[ymax], ylength]]
            if shot:
                gauss = lambda x, a, b, c: a*np.exp(-(x-b)**2/2*c**2)
                try:
                    xfitpara, xfitconv = curve_fit(gauss, xbin, xhist_percent)
                    xfit = gauss(xbin, *xfitpara)
                    xfitline = list(zip(xbin, xfit))
                except:
                    xfitline = list(zip(xbin, [0 for i in range(len(xbin))]))
                try:
                    yfitpara, yfitconv = curve_fit(gauss, ybin, yhist_percent)
                    yfit = gauss(ybin, *yfitpara)
                    yfitline = list(zip(ybin, yfit))
                except:
                    yfitline = list(zip(xbin, [0 for i in range(len(ybin))]))
                
                return_element.append(xfitline)
                return_element.append(yfitline)

            return_queue.put(return_element)