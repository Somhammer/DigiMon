import numpy as np
from scipy.optimize import curve_fit
import cv2

try:
    import cupy as cp
    CUPY_AVAILABLE = True
except ImportError:
    CUPY_AVAILABLE = False

import utilities as util
from variables import *

def stream_image(stream_queue, return_queue):
    while True:
        if not stream_queue.empty():
            element = stream_queue.get()
            if str(type(element[0])) == "<class 'str'>":
                if element[0] == 'EXIT': break
            image, para = element

            if image is None: continue
                
            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            image = util.filter_image(para, image)
            image = util.transform_image(para, image)
            image = util.slice_image(para, image)
            image = util.rotate_image(para, image)

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

            return_queue.put([image, xbin, ybin, xhist, yhist])

def analyze_image(analyze_queue, return_queue):
    useGPU = False
    if cv2.cuda.getCudaEnabledDeviceCount() > 0 and CUPY_AVAILABLE:
        try:
            cv2.cuda.setDevice(0)
            useGPU = True
        except Exception as e:
            print("GPU isn't available:", e)

    while True:
        if not analyze_queue.empty():
            element = analyze_queue.get()
            if str(type(element[0])) == "<class 'str'>":
                if element[0] == 'EXIT': break
            image, para = element

            if image is None: continue
                
            image = util.filter_image(para, image)
            image = util.transform_image(para, image)
            image = util.rotate_image(para, image)
            
            if len(image.shape) == 3:
                image = cv2.cuda.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            image = cv2.flip(image, 0)
            threshold = 0.05
            nypixel, nxpixel = image.shape

            if useGPU:
                g_image = cp.asarray(image)
                max_intensity = g_image.max()
                g_image = cp.where(g_image <= max_intensity*threshold, 0, g_image)

                image_center = cp.array([nxpixel//2, nypixel//2])

                pixel_per_mm = cp.array(para.pixel_per_mm)
                if para.calibrated:
                    p1, p2, p3, p4 = para.cal_dest_points.values()
                    p1 = cp.array(p1)
                    coordinate_center = cp.array([p1[0]]) - cp.abs(cp.array([p1[1]])) / pixel_per_mm  # pixel
                else:
                    coordinate_center = image_center

                roi = cp.asarray(para.roi)
                if para.roi_sel:
                    if len(roi) == 0 or roi[1] == cp.array([0, 0]) or roi == cp.array([[0, 0], [g_image.shape[1], g_image.shape[0]]]):
                        pass
                    else:
                        x, y, width, height = roi[0][0], roi[0][1], roi[1][0], roi[1][1]
                        src = image.copy()
                        g_image = src[y:y+height, x:x+width]
                    coordinate_center = coordinate_center - cp.array(para.roi[0])
                    nypixel, nxpixel = image.shape

                numerator = cp.array([0,0], dtype=cp.int64)
                denominator = cp.float64(0)

                y_indices, x_indices = cp.meshgrid(cp.arange(nypixel), cp.arange(nxpixel), indexing='ij')

                mask = g_image >= max_intensity * threshold
                numerator[0] = cp.sum(g_image[mask] * x_indices[mask])
                numerator[1] = cp.sum(g_image[mask] * y_indices[mask])
                denominator = cp.sum(g_image[mask])

                if denominator > 0:
                    center_pixel = numerator/denominator
                else:
                    return_queue.put(False)
                    return
                
                center_pixel = center_pixel - coordinate_center
                center_real = center_pixel / pixel_per_mm

                center_pixel = center_pixel - coordinate_center
                center_real = center_pixel / pixel_per_mm

                distances_from_center = cp.stack([x_indices - coordinate_center[0], y_indices - coordinate_center[1]])
                numerator[0] = cp.sum(g_image[mask] * cp.power((distances_from_center[0][mask] - center_pixel[0])/pixel_per_mm[0],2))
                numerator[1] = cp.sum(g_image[mask] * cp.power((distances_from_center[1][mask] - center_pixel[1])/pixel_per_mm[1],2))

                rms_beam_size = 2 * cp.sqrt(numerator/denominator)

                normalized_image = g_image / 255.0

                # xhist와 yhist 계산
                xhist = normalized_image.sum(axis=0) 
                yhist = normalized_image.sum(axis=1) 

                # xbin과 ybin 계산
                xminimum = -coordinate_center[0]/pixel_per_mm[0]  # mm
                yminimum = -coordinate_center[1]/pixel_per_mm[1]  # mm

                xbin = cp.linspace(xminimum, xminimum + (nxpixel-1)/pixel_per_mm[0], nxpixel)
                ybin = cp.linspace(yminimum, yminimum + (nypixel-1)/pixel_per_mm[1], nypixel)
                
                image = g_image.get()
                center_pixel = center_pixel.get()
                #center_pixel = np.array(int(round(center_pixel[0])), int(round(center_pixel[1])), dtype=int)
                center_real = center_real.get()
                rms_beam_size = rms_beam_size.get()
                xhist = xhist.get()
                yhist = yhist.get()
                xbin = xbin.get()
                ybin = ybin.get()
            else:
                max_intensity = image.max()
                image = np.where(image <= max_intensity*threshold, 0, g_image)

                # Calibration과 ROI 선택 처리
                if para.calibrated:            
                    p1, p2, p3, p4 = para.cal_dest_points.values()
                    p1 = np.array(p1)
                    coordinate_center = p1[0] - abs(p1[1]) / np.array(para.pixel_per_mm)
                else:
                    coordinate_center = image_center

                if para.roi_sel:
                    image = util.slice_image(para, image)
                    coordinate_center = coordinate_center - np.array(para.roi[0])

                numerator = np.array([0,0], dtype=np.int64)
                denominator = np.float64(0)

                y_indices, x_indices = np.meshgrid(np.arange(nypixel), np.arange(nxpixel), indexing='ij')

                mask = g_image >= max_intensity * threshold
                numerator[0] = np.sum(g_image[mask] * x_indices[mask])
                numerator[1] = np.sum(g_image[mask] * y_indices[mask])
                denominator = np.sum(g_image[mask])

                if denominator > 0:
                    center_pixel = numerator / denominator
                else:
                    return_queue.put(False)
                    return
                
                center_pixel = center_pixel - coordinate_center
                center_real = center_pixel / np.array(para.pixel_per_mm)
#                center_pixel = np.array(round(center_pixel[0]), round(center_pixel[1]))

                distances_from_center = np.stack([x_indices - coordinate_center[0], y_indices - coordinate_center[1]])
                numerator[0] = np.sum(g_image[mask] * np.power((distances_from_center[0][mask] - center_pixel[0])/pixel_per_mm[0],2))
                numerator[1] = np.sum(g_image[mask] * np.power((distances_from_center[1][mask] - center_pixel[1])/pixel_per_mm[1],2))

                rms_beam_size = 2 * np.sqrt(numerator/denominator)
                
                normalized_image = image / 255.0
                # xhist와 yhist 계산
                xhist = normalized_image.sum(axis=0) 
                yhist = normalized_image.sum(axis=1)  

                # xbin과 ybin 계산
                xminimum = -coordinate_center[0]/para.pixel_per_mm[0]  # mm
                yminimum = -coordinate_center[1]/para.pixel_per_mm[1]  # mm

                xbin = np.linspace(xminimum, xminimum + (nxpixel-1)/para.pixel_per_mm[0], nxpixel)
                ybin = np.linspace(yminimum, yminimum + (nypixel-1)/para.pixel_per_mm[1], nypixel)

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

            return_element = [para, image, xbin, ybin, xhist, yhist, xfitvalue, yfitvalue,
                center_pixel, center_real, [xwidth, xerror], [ywidth, yerror], rms_beam_size]
            return_queue.put(return_element)