#!/usr/bin/env python

import cv2
import argparse

def detectFace1(rgbimg):
    """
    Haar-like特徴量を用いたカスケード型分類器による顔検出(OpenCV)

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        target(list): 
    Reference:
        - https://self-development.info/opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98%E3%83%BB%E9%A1%94%E6%A4%9C%E5%87%BA%E3%82%92%E7%B0%A1%E5%8D%98%E3%81%AB%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95%E3%80%90python%E3%80%91/
        - https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
        - https://qiita.com/FukuharaYohei/items/ec6dce7cc5ea21a51a82
          - 動作原理の説明あり
    """
    XML_PATH = 'haarcascade_frontalface_default.xml'
    classifier = cv2.CascadeClassifier(XML_PATH)
    color = cv2.cvtColor(rgbimg, cv2.COLOR_BGR2GRAY)
    targets = classifier.detectMultiScale(color, scaleFactor=1.25)
    #targets = classifier.detectMultiScale(color)
    return targets

def detectFace2(rgbimg):
    """
    ResNet10ベースのSSDモデル(OpenCV Face Detector)による顔検出

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        target(list): 
    Reference:
        https://qiita.com/studio_haneya/items/97560b54b8348db8de87
        https://qiita.com/UnaNancyOwen/items/f3db189760037ec680f3

    """
    # TODO download model and config
    model = cv2.dnn_DetectionModel("opencv_face_detector.caffemodel", "opencv_face_detector.prototxt")
    model.setInputSize(300, 300)
    model.setInputMean((104.0, 177.0, 123.0))
    _, _, boxes = model.detect(image)
    return boxes

def detectFace3(rgbimg):
    """

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        target(list): 
    Reference:

    """
    pass

def show_image(rgbimg, targets):
    for x, y, w, h in targets:
       cv2.rectangle(rgbimg, (x, y), (x+w, y+h), (255, 0, 0), 2)
    while(1):
        cv2.imshow('result', rgbimg)
        key = cv2.waitKey(100) & 0xff
        if key != 255 or cv2.getWindowProperty('result', cv2.WND_PROP_AUTOSIZE) == -1:
            cv2.destroyAllWindows()
            exit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pic', help='specify the filepath of the picture')
    args = parser.parse_args()
    rgbimg = cv2.imread(args.input_pic)

    # detection
    out_rbgimg = rgbimg.copy()
    targets = detectFace1(rgbimg)
    #targets = detectFace2(rgbimg)

    # show image
    show_image(out_rbgimg, targets)

if __name__ == '__main__':
    main()