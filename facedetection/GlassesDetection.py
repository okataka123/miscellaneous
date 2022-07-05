#!/usr/bin/env python
import cv2
import argparse
from FaceDetection import show_image, detectFace1

def is_wearingGlasses1(rgbimg=None, bboxes=None):
    """
    (Non-ML)
    Determine whether or not people in the image are wearing glasses.
    Not Machine Learning method but image processing technique.

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
        bboxes(list): Bounding boxes for the number of people.
    Returns:
        results(list[bool]): list of True/False values of wearing glasses or not.
                             True: with glasses, False: without glasses
    Reference:
        - Webpage
         - https://medium.com/mlearning-ai/glasses-detection-opencv-dlib-bf4cd50856da
        - GitHub
         - https://github.com/siddh30/Glasses-Detection
    """
    import numpy as np
    import dlib
    import cv2
    import matplotlib.pyplot as plt
    from PIL import Image
    import statistics
    
    results = []
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') 

    for (x, y, w, h) in bboxes:
        rect = dlib.rectangle(x, y, x+w, y+h)
        # print('rect =', rect)
        # show_image(rgbimg, [(x, y, w, h)])
        
        sp = predictor(rgbimg, rect)
        landmarks = np.array([[p.x, p.y] for p in sp.parts()])

        nose_bridge_x = []
        nose_bridge_y = []
        for i in [28, 29, 30, 31, 33, 34, 35]:
            nose_bridge_x.append(landmarks[i][0])
            nose_bridge_y.append(landmarks[i][1])

        # x_min and x_max
        x_min = min(nose_bridge_x)
        x_max = max(nose_bridge_x)
        # ymin (from top eyebrow coordinate),  ymax
        y_min = landmarks[20][1]
        y_max = landmarks[31][1]

        rgbimg2 = Image.fromarray(rgbimg)
        rgbimg2 = rgbimg2.crop((x_min, y_min, x_max, y_max))
        img_blur = cv2.GaussianBlur(np.array(rgbimg2), (3, 3), sigmaX=0, sigmaY=0)
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        edges_center = edges.T[(int(len(edges.T)/2))]

        if 255 in edges_center:
            print("Glasses are present")
            results.append(True)
        else:
            print("Glasses are absent")
            results.append(False)
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pic', help='specify the filepath of the picture')
    args = parser.parse_args()
    rgbimg = cv2.imread(args.input_pic)
    
    bboxes = detectFace1(rgbimg)
    is_wearingGlasses1(rgbimg, bboxes)

if __name__ == '__main__':
    main()

"""
Note
Other refs

1. 
- Youtube
    https://www.youtube.com/watch?v=D8WakQq91sM
- GitHub
    https://github.com/devindatt/Custom-OpenCV-s-EyeGlass-Detector

2.

"""
