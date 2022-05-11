import numpy as np
from scipy.optimize import curve_fit
import cv2
from variables import *

def rotate_image(para, image):
    if para.rotation == 90:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif para.rotation == 180:
        image = cv2.rotate(image, cv2.ROTATE_180)
    elif para.rotation == 270:
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    if para.flip_rl == 1:
        image = cv2.flip(image, 1)
    
    if para.flip_ud == 1:
        image = cv2.flip(image, 0)

    return image

def filter_image(para, image):
    if para.filter_code == BKG_SUBSTRACTION:
        background = cv2.imread(para.filter_para['background file'])
        image = cv2.subtract(image, background)
    if para.filter_code == GAUSSIAN_FILTER:
        ksize = (para.filter_para['x kernal size'], para.filter_para['y kernal size'])
        sigmaX = para.filter_para['sigmaX']
        image = cv2.GaussianBlur(image, ksize=ksize, sigmaX=sigmaX)
    elif para.filter_code == MEDIAN_FILTER:
        ksize = para.filter_para['kernal size']
        image = cv2.medianBlur(image, ksize=ksize)
    elif para.filter_code == BILATERAL_FILTER:
        ksize = para.filter_para['kernal size']
        scolor = para.filter_para['sigma color']
        sspace = para.filter_para['sigma space']
        image = cv2.bilateralFilter(image, d=ksize, sigmaColor=scolor, sigmaSpace=sspace)
    else:
        image = image
    
    return image

def transform_image(para, image):
    if not para.calibrated: return
    
    if para.calibration_angle > 0.0:
        center = (round(image.shape[1]/2), round(image.shape[0]/2))
        angle = float(para.angle)
        matrix = cv2.getRotationMatrix2D(center, angle, 1)
        image = cv2.warpAffine(image, matrix, (0,0))

    if len(para.cal_target_points) == 0 or len(para.cal_destination_points) == 0: return
    
    transform_matrix = cv2.getPerspectiveTransform(np.float32(para.cal_target_points), np.float32(para.cal_destination_points))

    width, height = image.shape[1], image.shape[0]
    image = cv2.warpPerspective(image, transform_matrix, (width, height))
    
    return image

def slice_image(para, image):
    if len(para.roi) == 0 or para.roi[1] == [0,0] or para.roi == [[0,0], [image.shape[1], image.shape[0]]]: 
        return image

    x, y, width, height = para.roi[0][0], para.roi[0][1], para.roi[1][0], para.roi[1][1]
    src = image.copy()
    image = src[y:y+height, x:x+width]

    return image

def remove_white_noise(para, image):
    return image

def generate_transformation_matrix(para, image):
    if not len(image.shape) == 2: return
    if para.cal_target_points['Point1'] == para.cal_target_points['Point2']: return

    p1, p2, p3, p4 = para.cal_target_points.values()
    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)
    p4 = np.array(p4)

    avg = (abs(p1 - p2) + abs(p1 - p3) + abs(p1 - p4) + abs(p2 - p3) + abs(p2 - p4) + abs(p3 - p4))/6
    pixel_per_mm = avg[0] / avg[1]
    para.pixel_per_mm = pixel_per_mm.tolist()

    coordinate_center = np.array(p1[0]) - np.array(abs(p1[1]) / pixel_per_mm)
    para.coordinate_center = coordinate_center

    upper_left, lower_left, upper_right, lower_right = np.array([0,0]), np.array([0,0]), np.array([0,0]), np.array([0,0])
    points = [p1[0], p2[0], p3[0], p4[0]]
    for point in points:
        if point[0] < coordinate_center[0] and point[1] < coordinate_center[1]:
            upper_left = point
        elif point[0] < coordinate_center[0] and point[1] > coordinate_center[1]:
            lower_left = point
        elif point[0] > coordinate_center[0] and point[1] < coordinate_center[1]:
            upper_right = point
        else:
            lower_right = point

    #para.transform_matrix = cv2.getPerspectiveTransform(np.float32(para.original_points), np.float32(para.destination_points))

