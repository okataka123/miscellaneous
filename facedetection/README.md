# Face detection
画像からの顔検出の実験まとめ  
いろいろな手法・モデルを使って顔検出の精度について比較する。

## models
以下の表に検証model一覧を示す。

|No.|Pretrained-model|Description|Remarks|
|:-|:-|:-|:-|
|1|haarcascade_frontalface_default.xml|Haar-like特徴量を用いたカスケード型分類器による顔検出。非NN的な手法|-|
|2|-|HOG徴量とSVM識別器を用いた顔検出。非NN的な手法|-|
|3|opencv_face_detector.caffemodel <br> opencv_face_detector.prototxt|ResNet10ベースのSSDモデルを使った顔検出|-|
|4|yolov4.cfg <br> yolov4.weights|YOLOv4モデルを使った身体検出|顔検出モデルではなくて人物を身体ごと検出するモデル|
|5|yunet.onnx|YuNetによる顔検出|<font color=red>うまく動かない</font>|
|6|mmod_human_face_detector.dat|CNN|-|
|7|-|MTCNN|tensorflow 2.0がimportできる環境が必要。<br>推論に少し時間が掛かる。|

## 検証データについて
適当にWeb上で拾ってきた顔画像を検証用データとして用いる。またそれぞれの画像に対して、±15°、±30°、±45°、±60°、±90°に回転した画像も顔検出を試す。

## Results
---
### 0°
|Haar-like|HOGSVM|ResNet10base|dlibCNN|mtcnn|
|:-:|:-:|:-:|:-:|:-:|
|![01_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181934746-9386c099-3607-40b8-8050-828ba2167dd9.jpg)|![01_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181934761-8c334e59-13e5-4105-9152-0a530322b6e7.jpg)|![01_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181934777-aabdb34c-c06e-426a-a556-331e095030e6.jpg)|![01_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181934803-41dbc5f0-fdd7-4607-9ebb-c6d3794add78.jpg)|![01_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181934817-d2a63023-27e4-437f-b6ec-048055dadd28.jpg)|
|![02_bush_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181934867-fd8dd20c-742e-470d-b460-8b60b92b19be.jpg)|![02_bush_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181934875-b085de7b-d2c6-493f-8e67-071112ee7185.jpg)|![02_bush_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181934879-3ff0dca3-2ccb-4cd9-bd51-f294322b3066.jpg)|![02_bush_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181934888-550a3252-2d1b-4de8-8f24-1c9686904186.jpg)|![02_bush_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181934895-f49d2962-47a9-421f-861d-6718f28dc202.jpg)|
|![04_family_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181934929-eea91789-c32a-4aec-9fca-1c12765e32b3.jpg)|![04_family_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181934942-93bd8da5-b694-4d7b-b519-e5aa0d8bd3c4.jpg)|![04_family_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181934952-63f58779-49ac-42ce-a9ee-3fa39b90917e.jpg)|![04_family_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181934965-9c35cb7c-b773-4a81-9850-555944879519.jpg)|![04_family_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181934988-76066207-18cf-4475-a810-bb1223f22f97.jpg)|
|![05_glasses_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181935001-fa650c4e-fec8-469d-b64b-4ab16fbb34d1.jpg)|![05_glasses_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181935009-8685d57c-c342-4914-8d03-a8c04e536b3a.jpg)|![05_glasses_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181935016-8465f1d0-02db-4451-b93e-e3bc629b3c1e.jpg)|![05_glasses_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181935019-8291a820-61f6-43d8-bb07-fead3911a6a2.jpg)|![05_glasses_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181935034-58332e0a-2f4f-40d0-adc2-45fb42df9f2d.jpg)|
|![06_glasses_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181935078-edcfae45-1e5f-438a-8e45-98d613cd8153.jpg)|![06_glasses_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181935085-0af4f5f4-b5cc-4718-9111-6a3f39dd5b55.jpg)|![06_glasses_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181935093-9069bc37-a893-4e00-94f3-3c978d22ee94.jpg)|![06_glasses_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181935100-6d59f7b0-8273-4bfc-8e9e-a2aa06962ebf.jpg)|![06_glasses_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181935112-3c523d8a-0089-4ccf-bacd-5fed39d297f3.jpg)|
|![07_office_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181935121-275d4337-b388-478e-9eef-3f0a2d638bdf.jpg)|![07_office_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181935125-e54bbb8e-13d3-4105-8ac2-15deede7a431.jpg)|![07_office_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181935127-38fd4b91-e568-4b09-94fb-c96c544fb371.jpg)|![07_office_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181935130-aa3cd99f-36d4-4e16-bb00-dd50c743b66c.jpg)|![07_office_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181935132-3272847d-3d5a-4a05-88ca-55d5be394e2f.jpg)|
|![08_children_Haar-like_0deg](https://user-images.githubusercontent.com/41262277/181935168-557ed3df-0543-42b5-9372-55d1c3c7f36b.jpg)|![08_children_HOGSVM_0deg](https://user-images.githubusercontent.com/41262277/181935173-79c97e41-5bec-4480-917a-7447f59f5772.jpg)|![08_children_ResNet10base_0deg](https://user-images.githubusercontent.com/41262277/181935176-e5c6892a-392d-4c6c-ab05-2d917926d948.jpg)|![08_children_dlibCNN_0deg](https://user-images.githubusercontent.com/41262277/181935184-b5dbb6b3-458e-4c3c-af25-0f6cfbff7cb8.jpg)|![08_children_mtcnn_0deg](https://user-images.githubusercontent.com/41262277/181935191-2976d16f-e40e-46f2-82fd-9d5e9751b7a8.jpg)|

---
### 15° rotation
|Haar-like|HOGSVM|ResNet10base|dlibCNN|mtcnn|
|:-:|:-:|:-:|:-:|:-:|
|![01_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935365-3c166147-5fe1-4777-af2b-4d6e7e6dd271.jpg)|![01_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935370-12e3131a-9a45-4a91-bcec-118c9924b37b.jpg)|![01_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935374-7b6c0f98-7acc-4694-911c-baf1ae0fac7a.jpg)|![01_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935379-cf555dfe-88f8-41b8-8752-26d804999923.jpg)|![01_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935384-934b629f-2546-4f33-bbf3-3c8e2e326378.jpg)|
|![02_bush_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935454-ba95f5ad-3810-4af9-b66e-9e6ad3106b6c.jpg)|![02_bush_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935457-c862a8a6-e448-4ead-9215-1f6a49e9ff99.jpg)|![02_bush_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935461-fdb774d5-5b92-4b8c-9982-6206bf8e4d96.jpg)|![02_bush_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935464-e8f6572d-d6bd-4bc1-bc43-0afc9da7eb8d.jpg)|![02_bush_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935468-9c27a665-dfcc-4d86-8d87-bf4b673ecc71.jpg)|
|![04_family_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935523-6a229a19-3b7d-47f1-8e23-7c3ba59c1c54.jpg)|![04_family_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935526-0aebbbb3-936d-4a31-805f-0be51ee8ff93.jpg)|![04_family_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935527-0f5604e0-0e8d-4390-a4ac-552f39e536f1.jpg)|![04_family_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935530-372e10e0-efc1-482c-8800-e8df7d989ea9.jpg)|![04_family_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935531-eadf55b7-e696-47c8-8726-ecbcb0190c7b.jpg)|
|![05_glasses_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935572-f5a97d47-25cc-4f97-b4c3-c85f1a201e53.jpg)|![05_glasses_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935576-e2861c0c-3c56-4f77-883d-c1790c942c27.jpg)|![05_glasses_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935577-1b7a42f3-9287-433e-8ee9-d5d0a2a4dd70.jpg)|![05_glasses_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935578-a8a2efac-fc75-459c-bf03-2120abe8f969.jpg)|![05_glasses_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935579-fdaa05e5-8a41-444e-a6fa-b494a2f2e7cb.jpg)|
|![06_glasses_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935599-69b34738-7414-4cd9-9282-0815ad28bbe1.jpg)|![06_glasses_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935604-2d872a6e-a24f-479a-bf0f-38ec64d687e8.jpg)|![06_glasses_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935607-89dcb06c-76c4-4289-930c-6341d27d5a87.jpg)|![06_glasses_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935612-73b917ff-974a-428a-814e-a3c07625ef57.jpg)|![06_glasses_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935614-a1779821-b410-4a6d-b752-ef3be144433f.jpg)|
|![07_office_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935653-2bd7f014-ac97-4b68-a07e-bb21fa168ce1.jpg)|![07_office_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935654-81c3a94c-9e7b-4ba3-a22a-e2fd3daebdfc.jpg)|![07_office_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935656-0716644c-ba0d-48ec-9b2a-88e5b2aaba04.jpg)|![07_office_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935661-a55c7371-af7e-4e70-9976-0671b215addd.jpg)|![07_office_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935664-1349e085-69c8-4116-b674-85ca03f79f0e.jpg)|
|![08_children_Haar-like_15deg](https://user-images.githubusercontent.com/41262277/181935677-0d79c248-d320-45f7-b64f-94e6fc8dde97.jpg)|![08_children_HOGSVM_15deg](https://user-images.githubusercontent.com/41262277/181935680-f57e96fe-f9a1-44a4-ab3f-67f7a53cdc0f.jpg)|![08_children_ResNet10base_15deg](https://user-images.githubusercontent.com/41262277/181935682-d9b6ecef-f5b6-4333-a189-496705cb64ea.jpg)|![08_children_dlibCNN_15deg](https://user-images.githubusercontent.com/41262277/181935683-8a040f1f-4828-4649-bede-0bd9409fc503.jpg)|![08_children_mtcnn_15deg](https://user-images.githubusercontent.com/41262277/181935686-332f61b4-05c2-4758-8fc7-bbca5f3f66d2.jpg)|

---
### 30° rotation
|Haar-like|HOGSVM|ResNet10base|dlibCNN|mtcnn|
|:-:|:-:|:-:|:-:|:-:|
|![01_Haar-like_30deg](https://user-images.githubusercontent.com/41262277/181935730-aa953faf-7540-4b14-8607-40f64323ee2d.jpg)|![01_HOGSVM_30deg](https://user-images.githubusercontent.com/41262277/181935736-9c6dfad5-6bf3-44f9-b34a-ed8c7a73dbf6.jpg)|![01_ResNet10base_30deg](https://user-images.githubusercontent.com/41262277/181935739-d6afb50d-c112-4694-b3ab-c41c6bbbc7b7.jpg)|![01_dlibCNN_30deg](https://user-images.githubusercontent.com/41262277/181935742-5536eb0f-3979-4a19-b2a0-570bba32f79e.jpg)|![01_mtcnn_30deg](https://user-images.githubusercontent.com/41262277/181935745-6fc50ee8-0b12-4d86-a73c-635aac3b8af2.jpg)|
|![02_bush_Haar-like_30deg](https://user-images.githubusercontent.com/41262277/181935778-9a4826c0-372e-49bd-a935-00dc9c5edf52.jpg)|![02_bush_HOGSVM_30deg](https://user-images.githubusercontent.com/41262277/181935781-cf929667-d529-424d-85b3-40625d1697fb.jpg)|![02_bush_ResNet10base_30deg](https://user-images.githubusercontent.com/41262277/181935785-e8c0787c-2d05-4175-8019-d4dc066945fa.jpg)|![02_bush_dlibCNN_30deg](https://user-images.githubusercontent.com/41262277/181935787-d49bba2c-d54d-4d60-8683-27372f4742d8.jpg)|![02_bush_mtcnn_30deg](https://user-images.githubusercontent.com/41262277/181935790-d7e86856-a063-4732-af2a-ef6cb4e0c03a.jpg)|
|![04_family_Haar-like_30deg](https://user-images.githubusercontent.com/41262277/181935843-9933841f-d151-44f2-991c-480a83a62681.jpg)|![04_family_HOGSVM_30deg](https://user-images.githubusercontent.com/41262277/181935844-f9a9f42a-0622-40a9-b7f4-9f7fcf91ca35.jpg)|![04_family_ResNet10base_30deg](https://user-images.githubusercontent.com/41262277/181935851-1f837f45-60d8-4c6a-9270-b20eece6b8cc.jpg)|![04_family_dlibCNN_30deg](https://user-images.githubusercontent.com/41262277/181935853-936dc693-b78d-431e-9336-2ca8970626bd.jpg)|![04_family_mtcnn_30deg](https://user-images.githubusercontent.com/41262277/181935855-7f95d35c-ff68-4657-a7b6-83525559b0a1.jpg)|
|![05_glasses_Haar-like_30deg](https://user-images.githubusercontent.com/41262277/181935892-c91e1fff-ebce-42f0-8beb-e48629d9b8f8.jpg)|![05_glasses_HOGSVM_30deg](https://user-images.githubusercontent.com/41262277/181935898-ed7d1e08-b793-4839-ad7f-37502c41db8e.jpg)|![05_glasses_ResNet10base_30deg](https://user-images.githubusercontent.com/41262277/181935903-71b8d62a-dbf7-4140-b742-0374bc1a20c9.jpg)|![05_glasses_dlibCNN_30deg](https://user-images.githubusercontent.com/41262277/181935907-86325ee4-4336-4380-9cd7-cf1f51f8ff8e.jpg)|![05_glasses_mtcnn_30deg](https://user-images.githubusercontent.com/41262277/181935910-f08dab4f-fd12-4f7d-b197-3e8446b568cd.jpg)|
|![06_glasses_Haar-like_30deg](https://user-images.githubusercontent.com/41262277/181936103-788c152e-a469-408d-8fae-deb71b9c6179.jpg)|![06_glasses_HOGSVM_30deg](https://user-images.githubusercontent.com/41262277/181936106-dc7c85b6-2330-4fb5-94a2-7cabf5ff1f7b.jpg)|![06_glasses_ResNet10base_30deg](https://user-images.githubusercontent.com/41262277/181936111-e25cd98f-8f35-4cf9-8f01-c6b9f0d00cb5.jpg)|![06_glasses_dlibCNN_30deg](https://user-images.githubusercontent.com/41262277/181936113-7f5ec840-6d37-4bd8-9221-21a01a454fe3.jpg)|![06_glasses_mtcnn_30deg](https://user-images.githubusercontent.com/41262277/181936116-8869e524-9dcb-4653-930e-0e07d5fb9e4e.jpg)|


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
  - [photoAC](https://www.photo-ac.com/)
    - 写真のフリーサイト。適当な顔画像を探すのに使う。
