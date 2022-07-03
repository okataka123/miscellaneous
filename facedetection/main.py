#!/usr/bin/env python

import cv2
import argparse
from FaceDetection import detectFace1, show_image
from GlassesDetection import is_wearingGlasses1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pic', help='specify the filepath of the picture')
    args = parser.parse_args()
    rgbimg = cv2.imread(args.input_pic)

    # detection
    out_rbgimg = rgbimg.copy()
    bboxes = detectFace1(rgbimg)
    #bboxes = detectFace2(rgbimg)

    print('bboxes =', bboxes)
    
    # wearing glasses
    wgs = is_wearingGlasses1(out_rbgimg, bboxes)
    print('wgs =', wgs)

    # show image
    # show_image(out_rbgimg, bboxes)

if __name__ == '__main__':
    main()
