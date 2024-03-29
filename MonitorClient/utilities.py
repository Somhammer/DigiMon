import cv2

from variables import *

def rotate_image(para, image):
    if para.flip_rl == 1:
        image = cv2.flip(image, 1)
    
    if para.flip_ud == 1:
        image = cv2.flip(image, 0)

    if para.rotation != 0:
        matrix = cv2.getRotationMatrix2D((image.shape[1]/2, image.shape[0]/2), para.rotation, 1)
        image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

    return image

def filter_image(para, image):
    try:
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
    except:
        image = image
    
    return image

def transform_image(para, image):
    if not para.calibrated: return image

    #if para.cal_target_points['Point1'] == para.cal_target_points['Point2'] or para.cal_dest_points['Point1'] == para.cal_dest_points['Point2']: 
    #    return image
    
    #transform_matrix = cv2.getPerspectiveTransform(np.float32(para.cal_target_points), np.float32(para.cal_destination_points))

    width, height = image.shape[1], image.shape[0]
    image = cv2.warpPerspective(image, para.transform_matrix, (width, height))
    
    return image

def slice_image(para, image):
    if len(para.roi) == 0 or para.roi[1] == [0,0] or para.roi == [[0,0], [image.shape[1], image.shape[0]]]: 
        return image

    x, y, width, height = para.roi[0][0], para.roi[0][1], para.roi[1][0], para.roi[1][1]
    src = image.copy()
    image = src[y:y+height, x:x+width]

    return image

# FIXME
def remove_white_noise(para, image):
    return image
