# Face detection
画像からの顔検出の実験まとめ  
いろいろな手法・モデルを使って顔検出の精度について比較する。

## models
以下の表に検証model一覧を示す。

|No.|model|description|
|:-|:-|:-|
|1|haarcascade_frontalface_default.xml|Haar-like特徴量を用いたカスケード型分類器による顔検出。非NN的な手法|
|2||HOG特徴量とSVM識別器を用いた顔検出。非NN的な手法|
|3|opencv_face_detector.caffemodel <br> opencv_face_detector.prototxt|ResNet10ベースのSSDモデルを使った顔検出|
|4|yolov4.cfg <br> yolov4.weights|YOLOv4モデルを使った顔検出|
|5|yunet.onnx|YuNetによる顔検出|
|6||CNN|
|7||MTCNN|

## 検証dataについて
適当にWeb上で拾ってきた顔画像を検証用データとして用いる。またそれぞれの画像に対して、±15°、±30°、±45°、±60°、±90°に回転した画像も顔検出を試す。

## References
  - [【入門者向け解説】openCV顔検出の仕組と実践(detectMultiScale)](https://qiita.com/FukuharaYohei/items/ec6dce7cc5ea21a51a82)
    - Haar-like特徴量を用いたカスケード型分類器による顔検出に関する原理の説明。

  - [OpenCVの新しい顔検出を試してみる](https://qiita.com/UnaNancyOwen/items/f3db189760037ec680f3)
    - このページでは、従来のHaar-like特徴量を用いたカスケード型分類器による顔検出や、ResNet10ベースのSSDモデル（OpenCV Face Detector）による顔検出に加え、YuNetによる顔とランドマークの検出方法について記載されている。

  - [OpenCVでDNN](https://ws.tetsuakibaba.jp/doku.php?id=opencv_dnn:%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89:install)
  - [サンプルを動作させる](https://ws.tetsuakibaba.jp/doku.php?id=opencv_dnn:samples:%E6%9C%80%E5%88%9D%E3%81%AB)
    - 上記2つのリンクでは、OpenCVでDNNを動かすための方法について詳しく説明している。



  - [OpenCVで顔検出する](https://qiita.com/studio_haneya/items/97560b54b8348db8de87)
    - YOLOv4のモデルを使ったNNベースの顔検出の説明がある。

  - [OpenCVの新しい顔認識を試してみる](https://qiita.com/UnaNancyOwen/items/8c65a976b0da2a558f06)
    - こちらは顔認識なので、顔検出とは少し違う。


  - [4種類の顔検出を動かしてみた　[ Haar+Cascade/ HOG+SVM/ CNN/ MTCNN ]](https://iatom.hatenablog.com/entry/2020/11/01/152307)
  - [顔の傾き（Roll）で顔検出を検証してみた](https://iatom.hatenablog.com/entry/2020/11/05/215247)
    - 上記2つのリンクでは、以下の4つの手法で顔検出の検証をしている。
      - Haar-like 特徴量＋Cascade 識別器
      - Dlib（HOG特徴量＋SVM識別器）
      - CNN（mmod_human_face_detector.dat.bz2）
      - MTCNN（Multi-task Cascaded Convolutional Neural Networks for Face Detection）
    - また、上記2つのリンクのうち下側では、これら4種類のモデルで顔画像を回転させたときの検出精度も比較している。

  - [OpenCV Haar-Cascadeによる顔検出](https://qiita.com/tnoce/items/c819c85a85c16d246be8)

  - [[OpenCV+dlib] 顔認識の実験](https://qiita.com/kotai2003/items/fb1f35da5437eefbc5da)
    - dlibのライブラリを

  - [調和技研 技術ブログ OpenCVとdlibの顔検出機能の比較](https://blog.chowagiken.co.jp/entry/2019/06/28/OpenCV%E3%81%A8dlib%E3%81%AE%E9%A1%94%E6%A4%9C%E5%87%BA%E6%A9%9F%E8%83%BD%E3%81%AE%E6%AF%94%E8%BC%83)