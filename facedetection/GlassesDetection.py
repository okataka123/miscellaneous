#!/usr/bin/env python
import cv2

def is_wearingGlasses1(rgbimg=None, bboxes=None):
    """
    (Non-ML)

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
        bboxes(list): Bounding boxes for the number of people.
    Returns:
        results(list[bool]): list of True/False values of wearing glasses or not.
                             True: メガネあり、False: メガネなし
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
   
    # for debug 本来はRBGデータのままもらう
#    path = 'pics/01.jpg'
#    path = 'pics/02_bush.jpg'
#    path = 'pics/03_bush.jpg'
#    path = 'pics/04_family.jpg'
#    path = 'pics/05_glasses.jpg'
#    path = 'pics/06_glasses.jpg'
#    rgbimg = dlib.load_rgb_image(path)

    for (x, y, w, h) in bboxes:
        cutted_rgbimg = rgbimg[y:y+h, x:x+w] # cutすると顔が検知できなくなる。(05の画像の場合)
        # cutted_rgbimg = rgbimg # cut

        if len(detector(cutted_rgbimg))==0:
            print('No face detected')
            results.append(False)
            continue
        
        rect = detector(cutted_rgbimg)[0]
        sp = predictor(cutted_rgbimg, rect)
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

        cutted_rgbimg2 = Image.fromarray(cutted_rgbimg)
        cutted_rgbimg2 = cutted_rgbimg2.crop((x_min, y_min, x_max, y_max))

        img_blur = cv2.GaussianBlur(np.array(cutted_rgbimg2), (3, 3), sigmaX=0, sigmaY=0)
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        edges_center = edges.T[(int(len(edges.T)/2))]

        if 255 in edges_center:
            print("Glasses are present")
            results.append(True)
        else:
            print("Glasses are absent")
            results.append(False)
    return results


def is_wearingGlasses2(rgbimg=None, bboxes=None):
    """
    (Non-ML)
    Under constructing....

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
        bboxes(list): 
    Returns:
        results(list[bool]):
                            True: メガネあり、False: メガネなし
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
    import inspect

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') 
   
    # for debug 本来はRBGデータのままもらう
#    path = 'pics/01.jpg'
#    path = 'pics/02_bush.jpg'
#    path = 'pics/03_bush.jpg'
#    path = 'pics/04_family.jpg'
    path = 'pics/05_glasses.jpg'
#    path = 'pics/06_glasses.jpg'
    rgbimg = dlib.load_rgb_image(path)

    if len(detector(rgbimg))==0:
        print('No face detected')
        return('No face detected')
    
    p = detector(rgbimg)
    print('detector(rgbimg) =', detector(rgbimg))
    print('type(detector(rgbimg)) =', type(detector(rgbimg)))
    # detector
    print('p =', p)
    print('p[0] =', p[0])
    print('p[0].top =', p[0].top)
    a = np.array(p[0])
    print('a =', a)
#    for x in inspect.getmembers(p[0], inspect.ismethod):
#        print(x[0])

    cv2.rectangle(rgbimg, (328, 161), (543, 376), (255, 0, 0), 2)
    show_image(rgbimg)


    


    rect = detector(rgbimg)[0]
    sp = predictor(rgbimg, rect)
    landmarks = np.array([[p.x, p.y] for p in sp.parts()])

    nose_bridge_x = []
    nose_bridge_y = []

    for i in [28,29,30,31,33,34,35]:
        nose_bridge_x.append(landmarks[i][0])
        nose_bridge_y.append(landmarks[i][1])

    # x_min and x_max
    x_min = min(nose_bridge_x)
    x_max = max(nose_bridge_x)

    # ymin (from top eyebrow coordinate),  ymax
    y_min = landmarks[20][1]
    y_max = landmarks[31][1]

    img2 = Image.open(path)
    img2 = img2.crop((x_min,y_min,x_max,y_max))

    img_blur = cv2.GaussianBlur(np.array(img2),(3,3), sigmaX=0, sigmaY=0)
    edges = cv2.Canny(image =img_blur, threshold1=100, threshold2=200)
    edges_center = edges.T[(int(len(edges.T)/2))]

    if 255 in edges_center:
        print("Glasses are present")
        return True
    else:
        print("Glasses are absent")
        return False

def main():
    is_wearingGlasses1()

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
