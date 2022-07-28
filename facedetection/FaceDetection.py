#!/usr/bin/env python
import cv2
import dlib
import copy
import argparse
from mtcnn import MTCNN
import numpy as np
import matplotlib.pyplot as plt

def detectFace_HaarlikeFeature(rgbimg):
    """
    Haar-like特徴量を用いたカスケード型分類器による顔検出(OpenCV)

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(numpy.ndarray): sets of bounding box for face regions.
    Reference:
        - https://self-development.info/opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98%E3%83%BB%E9%A1%94%E6%A4%9C%E5%87%BA%E3%82%92%E7%B0%A1%E5%8D%98%E3%81%AB%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95%E3%80%90python%E3%80%91/
        - https://note.nkmk.me/python-opencv-face-detection-haar-cascade/
        - https://qiita.com/FukuharaYohei/items/ec6dce7cc5ea21a51a82
          - 動作原理の説明あり
    """
    XML_PATH = 'models/haarcascade_frontalface_default.xml'
    classifier = cv2.CascadeClassifier(XML_PATH)
    color = cv2.cvtColor(rgbimg, cv2.COLOR_BGR2GRAY)
    bboxes = classifier.detectMultiScale(color, scaleFactor=1.25)
    #bboxes = classifier.detectMultiScale(color)
    return bboxes

def detectFace_HOGSVM(rgbimg):
    """
    HOG特徴量+SVMによる顔検出(dlib)

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(dlib.rectangles): sets of bounding box for face regions.
    Reference:
        - https://qiita.com/kotai2003/items/fb1f35da5437eefbc5da
        - https://iatom.hatenablog.com/entry/2020/11/01/152307
    """
    detector = dlib.get_frontal_face_detector()
    bboxes = detector(rgbimg, 1)
    return bboxes

def detectFace_ResNet10base(rgbimg):
    """
    ResNet10ベースのSSDモデル(OpenCV Face Detector)による顔検出

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(numpy.ndarray): sets of bounding box for face regions.
    Reference:
        ## https://qiita.com/studio_haneya/items/97560b54b8348db8de87
        https://qiita.com/UnaNancyOwen/items/f3db189760037ec680f3

    """
    model = cv2.dnn_DetectionModel("models/opencv_face_detector.caffemodel", "models/opencv_face_detector.prototxt")
    model.setInputSize(300, 300)
    model.setInputMean((104.0, 177.0, 123.0))
    _, _, bboxes = model.detect(rgbimg)
    return bboxes

def detectFace_YOLOv4(rgbimg):
    """
    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(): sets of bounding box for face regions.
    Reference:

    Note:
        - The size of yolov4.weights is too large, this file is
          out of control.'yolov4.weights' and 'yolov4.cfg' can be
          downloarded from the following URL.
          https://github.com/AlexeyAB/darknet/wiki/YOLOv4-model-zoo

        - This model is not for detection of Face but for person's entire body.
    """
    model = cv2.dnn_DetectionModel("models/yolov4.weights", "models/yolov4.cfg")
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    _, _, bboxes = model.detect(rgbimg, confThreshold=0.6, nmsThreshold=0.4)
    return bboxes

def detectFace_YuNet(rgbimg):
    """
    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(): sets of bounding box for face regions.
    Reference:

    Note:
        - 'yunet.onnx' can be downloaded from the following URL.
          https://github.com/ShiqiYu/libfacedetection.train/blob/a61a428929148171b488f024b5d6774f93cdbc13/tasks/task1/onnx/yunet.onnx
        - うまく動かない！！
    """
    height, width, _ = rgbimg.shape
    #model = cv2.FaceDetectorYN.create("models/yunet.onnx", "", (width, height))
    model = cv2.FaceDetectorYN.create("models/yunet.onnx", "", (0, 0))
    #model = cv2.FaceDetectorYN.create("models/yunet_yunet_final_640_640_simplify.onnx", "", (0, 0))
    model.setInputSize((width, height))
    _, bboxes = model.detect(rgbimg)
    return bboxes

def detectFace_cnn(rgbimg):
    """
    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(dlib.mmod_rectangles): sets of bounding box for face regions.
    Reference:
    Note:
        - 'mmod_human_face_detector.dat' is in the following URL.
          https://github.com/davisking/dlib-models
    TODO:
        - CNNってどんなCNNを調べる。
    """
    cascade = dlib.cnn_face_detection_model_v1('models/mmod_human_face_detector.dat')
    bboxes = cascade(rgbimg, 1)
    return bboxes

def detectFace_mtcnn(rgbimg):
    """
    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(): sets of bounding box for face regions.
    Reference:
    Note:
        tensorflowがimportできる環境が必要。
    """
    detector = MTCNN()
    info = detector.detect_faces(rgbimg)
    bboxes = []
    for d in info:
        bboxes.append(d['box'])
    return bboxes

def detectFace_template(rgbimg):
    """
    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
    Returns:
        bboxes(): sets of bounding box for face regions.
    Reference:
    Note:
    """
    return bboxes

def rotate(rgbimg, theta, center=None):
    '''
    rotate the image by the specified angle.

    Args:
        rgbimg(numpy.ndarry): rgbdata of one picture.
        thera(int): rotation angle.
        center(int): center of rotation.
    Returns:
        rotated_rgbimg(numpy.ndarry): rotated rgbdata.
    '''
    height = rgbimg.shape[0]
    width = rgbimg.shape[1]
    out_rgbimg = copy.deepcopy(rgbimg)
    if center is None:
        center = (int(width/2), int(height/2))
    scale = 1.0
    trans = cv2.getRotationMatrix2D(center, theta, scale)
    out_rgbimg = cv2.warpAffine(rgbimg, trans, (width, height))
    return out_rgbimg

def show_image_withbb(rgbimg, bboxes=None):
    if bboxes is not None:
        for (x, y, w, h) in bboxes:
           cv2.rectangle(rgbimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
    while(1):
        cv2.imshow('result', rgbimg)
        key = cv2.waitKey(100) & 0xff
        if key != 255 or cv2.getWindowProperty('result', cv2.WND_PROP_AUTOSIZE) == -1:
            cv2.destroyAllWindows()
            exit()

def show_image_withbb_nb(rgbimg, bboxes=None):
    '''
    Jupyter Notebook上でbounding box付きの画像を表示する。
    bboxesがNoneのときは、そのまま画像を表示する。

    Reference:
        - How to convert mmod_rectangles to rectangles via Dlib?
          https://stackoverflow.com/questions/56322815/how-to-convert-mmod-rectangles-to-rectangles-via-dlib 
    '''
    out_rgbimg = copy.deepcopy(rgbimg)
    if bboxes is not None:
        if type(bboxes) == np.ndarray:
            for (x, y, w, h) in bboxes:
                cv2.rectangle(out_rgbimg, (x, y), (x+w, y+h), (0, 255, 0), 2)
        elif type(bboxes) == dlib.rectangles:
            for bbox in bboxes:
                x1 = bbox.left()
                y1 = bbox.top()
                x2 = bbox.right()
                y2 = bbox.bottom()
                cv2.rectangle(out_rgbimg, (x1, y1), (x2, y2), (0, 255, 0), 2)
        elif type(bboxes) == dlib.mmod_rectangles:
            for bbox in bboxes:
                x1 = bbox.rect.left()
                y1 = bbox.rect.top()
                x2 = bbox.rect.right()
                y2 = bbox.rect.bottom()
                cv2.rectangle(out_rgbimg, (x1, y1), (x2, y2), (0, 255, 0), 2)
        elif type(bboxes) == list:
            for bbox in bboxes:
                x1 = bbox[0]
                y1 = bbox[1]
                x2 = bbox[0] + bbox[2]
                y2 = bbox[1] + bbox[3]
                cv2.rectangle(out_rgbimg, (x1, y1), (x2, y2), (0, 255, 0), 2)
    plt.imshow(out_rgbimg)
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pic', help='specify the filepath of the picture')
    args = parser.parse_args()
    rgbimg = cv2.imread(args.input_pic)
    bboxes = detectFace_HaarlikeFeature(rgbimg)
    #bboxes = detectFace_ResNet10base(rgbimg)
    print('bboxes =', bboxes)

if __name__ == '__main__':
    main()
    
