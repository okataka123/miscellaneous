# 機械学習を始めるための参考文献集
## 機械学習とは？
  - [人工知能と機械学習 - 総務省](https://www.soumu.go.jp/ict_skill/pdf/ict_skill_3_5.pdf)
    - 総務省から出ている機械学習俯瞰用スライド。意外とまとまっているが、文字が多い…
  - [Qiita記事 機械学習超入門](https://qiita.com/ishizakiiii/items/d422019b52d973e0e28d)
    - 読み物。機械学習のおおざっぱな概要がつかめる。
  - [Qiita記事 一から始める機械学習（機械学習概要）](https://qiita.com/taki_tflare/items/42a40119d3d8e622edd2)
    - 読み物。機械学習のおおざっぱな概要がつかめる。
  - [Qiita記事 10分で分かるAIの歴史](https://qiita.com/cr-fun/items/adf0f7f405eeebc42a50)

## 機械学習入門
  - [東工大 機械学習帳](https://chokkan.github.io/mlnote/index.html)
    - Jupyter Notebook形式で読める、"動く"機械学習帳。機械学習の基礎となる単回帰・重回帰から始まり、理論的な説明と実際のデータを使った確認が同時になされているため、体系的に勉強することができる。（ただし、誤差逆伝播の理論的説明が少ないため、その後の自動微分の話が少し分かりにくい？）

## Neural Network関連
とりあえず、以下のとてもわかり易い一連のQiita記事を全て読みましょう！
  - [Qiita記事 深層学習入門 \~基礎編\~](https://qiita.com/kuroitu/items/221e8c477ffdd0774b6b)
  - [Qiita記事 深層学習入門 \~コーディング準備編\~](https://qiita.com/kuroitu/items/884c62c48c2daa3def08)
  - [Qiita記事 深層学習入門 \~順伝播編\~](https://qiita.com/kuroitu/items/d22c8750e34d5d75fb6c)
  - [Qiita記事 深層学習入門 \~逆伝播編\~](https://qiita.com/kuroitu/items/ea6ed8f614e65ec44976)
  - [Qiita記事 深層学習入門 \~学習則編\~](https://qiita.com/kuroitu/items/ab5ad4ac716ae7a04891)
  - [Qiita記事 深層学習入門 \~ローカライズと損失関数編\~](https://qiita.com/kuroitu/items/a6725ac0139d8eeb1e19)
  - [Qiita記事 深層学習入門 \~関数近似編\~](https://qiita.com/kuroitu/items/4a8badcf7d3139d9ec7b)
  - [Qiita記事 深層学習入門 \~畳み込みとプーリング編\~](https://qiita.com/kuroitu/items/48bf6bc42e4dfee52cde)
  - [Qiita記事 深層学習入門 \~CNN実験編\~](https://qiita.com/kuroitu/items/d4716e754594a29b059d)
  - [Qiita記事 深層学習外伝 \~GPUプログラミング編\~](https://qiita.com/kuroitu/items/2618c598f46d6ab3889c)
  - [Qiita記事 深層学習入門 \~ドロップアウト編\~](https://qiita.com/kuroitu/items/d1bed8c216950d87be74)
  - [Qiita記事 活性化関数一覧 (2020)](https://qiita.com/kuroitu/items/73cd401afd463a78115a)
  - [Qiita記事 勾配降下法一覧 (2020)](https://qiita.com/kuroitu/items/36a58b37690d570dc618)
  - [Qiita記事 見てわかる！最適化手法の比較 (2020)](https://qiita.com/kuroitu/items/6695e0c79e888543e150)

### CNN関連
  - [Qiita記事 Convolutional Neural Networkとは何なのか](https://qiita.com/icoxfog417/items/5fd55fad152231d706c2)
  - [定番のConvolutional Neural Networkをゼロから理解する](https://deepage.net/deep_learning/2016/11/07/convolutional_neural_network.html)
  - [第4回　CNN（Convolutional Neural Network）を理解しよう（TensorFlow編）](https://atmarkit.itmedia.co.jp/ait/articles/1804/23/news138.html)
  - [Qiita記事 畳み込みニューラルネットワークの最新研究動向 (〜2017)](https://qiita.com/yu4u/items/7e93c454c9410c4b5427)
    - ちょっと情報が古いが、CNNベースの有名Netについて俯瞰できる。

### RNN関連
  - [Qiita記事 LSTMネットワークの概要](https://qiita.com/KojiOhki/items/89cd7b69a8a6239d67ca) 
  - [Qiita記事 わかるLSTM ～ 最近の動向と共に](https://https://qiita.com/t_Signull/items/21b82be280b46f467d1bqiita.com/t_Signull/items/21b82be280b46f467d1b)
    - LSTMの歴史がわかる。CEC(Constant Error Carousel)については第一世代LSTMが発表された1997年当時からすでにあった。しかし、Forgot GateやPeephole Connection、Full Gradientについては初めから導入されていたわけではなく、LSTMの進化とともに徐々に導入されていった経緯が理解できる。
  - [GRU(Gated Recurrent Unit)](https://cvml-expertguide.net/terms/dl/rnn/gru/)

### AutoEncoder関連
  - [Qiita記事 Variational Autoencoder徹底解説](https://qiita.com/kenmatsu4/items/b029d697e9995d93aa24)
  - []()
  （T.B.D.　PCAやt-SNEなどの多様体学習もこの欄に追加する？）

### GAN関連
T.B.D.
  - []()

### Attension・Transformer関連
  - [Qiita記事 深層学習界の大前提Transformerの論文解説！](https://qiita.com/omiita/items/07e69aef6c156d23c538)
  - [Qiita記事 作って理解する Transformer / Attention](https://qiita.com/halhorn/items/c91497522be27bde17ce)

### GNN (Graph Neural Network)関連
 - [Math Behind Graph Neural Networks](https://rish-16.github.io/posts/gnn-math/)
   - GNNのtutorial。Twitterで発見。元ツイは[コレ](https://twitter.com/rishabh16_/status/1505600925926260739)

## 教師なし学習(特にNeural以外の手法)
T.B.D.

T.B.D.
## 強化学習
  - [Qiita記事 DQN（Deep Q Network）を理解したので、Gopherくんの図を使って説明](https://qiita.com/ishizakiiii/items/5eff79b59bce74fdca0d)
  - [Qiita記事 ゼロからDeepまで学ぶ強化学習](https://qiita.com/icoxfog417/items/242439ecd1a477ece312)
T.B.D.

## Advanced
  - [Qiita記事 【まとめ】ディープラーニングを使った異常検知](https://qiita.com/shinmura0/items/06d81c72601c7578c6d3)
    - [@shinmura0](https://twitter.com/shinmura0)さんによる異常検知まとめ。
  - [Qiita記事 物体検出についての歴史まとめ(1)](https://qiita.com/mshinoda88/items/9770ee671ea27f2c81a9)
  - [Qiita記事 物体検出についての歴史まとめ(2)](https://qiita.com/mshinoda88/items/c7e0967923e3ed47fee5)
  - [Qiita記事 モダンな深層距離学習 (deep metric learning) 手法: SphereFace, CosFace, ArcFace](https://qiita.com/yu4u/items/078054dfb5592cbb80cc)
    - metric learningについてまとまっている。特にArcFaceはしっかり抑えておく。
  - [学習する天然ニューラルネット Confident Learning -そのラベルは正しいか？](https://aotamasaki.hatenablog.com/entry/confident_learning)
    - 世の中の教師ラベルはだいたいnoisy.　そいういうときはどうすればいいか？という話。
  - [Noisy label 対抗記 \~Cassava Leaf Disease Classification\~ / Diary against the noisy label](https://speakerdeck.com/sansandsoc/diary-against-the-noisy-label)
    - これもnoisy labelの話。
  - [u++の防備録 Adversarial Validationを用いた特徴量選択](https://upura.hatenablog.com/entry/2019/10/27/211137)
    - trainデータとtestデータで分布が大きく大きく異なるときはどうすればいいか？その一つの方法が"Adversarial Varidation"
  - [Qiita記事 adversarial validationを実装してみた](https://qiita.com/shota-imazeki/items/6f48c78edf0ce3b316e1#:~:text=adversarial%20validation%E3%81%A8%E3%81%AF%E3%80%81train,%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82)
  - [Kaggleで役立つAdversarial Validationとは](https://www.acceluniverse.com/blog/developers/2020/01/kaggleadversarial-validation.html)

## 数学系
### 数理最適化
  - [東工大 水野研究室 学習・研究用テキスト(最適化,線形計画法,内点法,数理計画法)](http://www.me.titech.ac.jp/~mizu_lab/text.html)
    - 線形計画法、非線型計画法、内点法などをテーマとした講義pdfが配布されている。
  - [『パターン認識と機械学習の学習 普及版』](herumi.github.io/prml/)
    - PRMLの数式理解に必要な数学を丁寧にまとめたpdf


## Others
  - [機械学習他】【長期】Qiitaの今読んでおくべき記事１００選【毎週自動更新】](https://qiita.com/j5c8k6m8/items/481b221277d9355934a0) 
    - このメモに挙げているURLたちも、いくつかはココで整理されているものを参考にした。
  - [Qiita記事 誤差逆伝播法のノート](https://qiita.com/Ugo-Nama/items/04814a13c9ea84978a4c)
    - 誤差逆伝播(Backpropagation)について詳細を忘れたときに読む記事。
  - [Qiita記事 機械学習エンジニアに爆速でなるための教材集](https://qiita.com/KangsooKim/items/8d987a7089297068477b)
  - [東大 2019年度講義 数理手法Ⅶ](https://ocwx.ocw.u-tokyo.ac.jp/course_11416/)
    - 古典的な時系列解析について講義動画が体系的にまとめられている。

## 書籍など
  - [実践Data Scienceシリーズ PythonではじめるKaggleスタートブック](https://www.amazon.co.jp/%E5%AE%9F%E8%B7%B5Data-Science%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8BKaggle%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%83%96%E3%83%83%E3%82%AF-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E7%A5%A5%E5%A4%AA%E9%83%8E/dp/4065190061)
    - upuraさんとカレーさんの本
  - [機械学習スタートアップシリーズ これならわかる深層学習入門](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E3%81%93%E3%82%8C%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%E5%85%A5%E9%96%80-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E7%80%A7-%E9%9B%85%E4%BA%BA/dp/4061538284/ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3FBF5SFUM1SU7&keywords=%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92&qid=1649951148&s=books&sprefix=%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%2Cstripbooks%2C251&sr=1-6)
    - 初めて全部読んだ本がコレ。
  - [機械学習スタートアップシリーズ ベイズ推論による機械学習入門](https://www.amazon.co.jp/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88%E3%82%A2%E3%83%83%E3%83%97%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-%E3%83%99%E3%82%A4%E3%82%BA%E6%8E%A8%E8%AB%96%E3%81%AB%E3%82%88%E3%82%8B%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E5%85%A5%E9%96%80-KS%E6%83%85%E5%A0%B1%E7%A7%91%E5%AD%A6%E5%B0%82%E9%96%80%E6%9B%B8-%E9%A0%88%E5%B1%B1-%E6%95%A6%E5%BF%97/dp/4061538322/ref=sr_1_3?adgrpid=109848114171&gclid=Cj0KCQjwjN-SBhCkARIsACsrBz5qQu5grukqCIXSz_qRb7j2cD9esDBhjQlh9uDAyN6lSRY24Dgwe28aAtkFEALw_wcB&hvadid=448041872863&hvdev=c&hvlocphy=1009332&hvnetw=g&hvqmt=e&hvrand=2011472433856026341&hvtargid=kwd-376617406059&hydadcr=27266_11561146&jp-ad-ap=0&keywords=%E3%81%93%E3%82%8C%E3%81%AA%E3%82%89%E3%82%8F%E3%81%8B%E3%82%8B%E6%B7%B1%E5%B1%A4%E5%AD%A6%E7%BF%92%E5%85%A5%E9%96%80&qid=1649951171&sr=8-3)
    - ベイス推定の本。5章以降が難しかったので放置。
  - [Kaggleで勝つデータ分析の技術](https://www.amazon.co.jp/Kaggle%E3%81%A7%E5%8B%9D%E3%81%A4%E3%83%87%E3%83%BC%E3%82%BF%E5%88%86%E6%9E%90%E3%81%AE%E6%8A%80%E8%A1%93-%E9%96%80%E8%84%87-%E5%A4%A7%E8%BC%94/dp/4297108437/ref=sr_1_1_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=IT2I90OL924B&keywords=kaggle&qid=1649951366&sprefix=kaggle%E6%9C%AC%2Caps%2C191&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyS09PM0lWNU00RjRRJmVuY3J5cHRlZElkPUEwMjQ4Mjc1WFUyRkVCSElDMEhLJmVuY3J5cHRlZEFkSWQ9QTFJRkQ0UFo2VVRDOUYmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl)
    - 必読本だが余り読めてない。。

## 動画
  - [[Youtube] Neural Network Console](https://www.youtube.com/c/NeuralNetworkConsole)
    - Sonyによる深層学習をテーマとしたレクチャー動画集。それぞれの動画は長くても10分程度と短いので見やすい。
  - [[Youtube] AIcia Solid Project](https://www.youtube.com/channel/UC2lJYodMaAfFeFQrGUwhlaQ)
    - VTuberによって機械学習や数学をテーマに数多くの動画が公開されているYoutubeチャネル。個人的にはベイズ統計シリーズが分かりやすかった。
  - [[Youtube] nnabla ディープラーニングチャンネル](https://www.youtube.com/channel/UCOELxR-yS2EbjBxQ0hx4yBw)
    - nnablaによるYoutubeチャネルであり、学会聴講まとめや最新論文の解説などの動画がまとめられている。かなりAdvancedな内容だがとても勉強になる。特に[【Deep Learning研修（発展）】系列データモデリング (RNN / LSTM / Transformer)　第７回「Transformer」](https://www.youtube.com/watch?v=oVEkXMu4e-s)がオススメ
  - [[Youtube] How to get meaning from text with language model BERT | AI Explained](https://www.youtube.com/watch?v=-9vVhYEXeyQ)
    - Transformerの概要について3Dアニメーションで説明している。

## データ分析コンペサイト
  - [kaggle](https://www.kaggle.com/)
    - 運営元：Google （米国）
    - 世界最大規模のデータ分析コンペティションプラットフォームである
  - [SIGNATE](https://signate.jp/)
    - 運営元：株式会社SIGNATE（日本）
    - 日本語のプラットフォームなので、英語が苦手でも参加できる
  - [Nishika](https://www.nishika.com/)
    - 運営元：Nishika株式会社（日本）
    - 2019年12月にオープンした、日本語で参加できるプラットフォームである
  - [DrivenData](https://www.drivendata.org/)
    - 運営元：DrivenData Inc.（米国）
    - 社会課題の解決に特化したプラットフォームである
  - [CrowdAnalytix](https://www.crowdanalytix.com/)
    - 運営元：CrowdANALYTIX（インド）
    - データサイエンティストコミュニティ活用企業が主催のデータ分析コンペである
  - [Tianchi Big Data Competition](https://tianchi.aliyun.com/competition/gameList/activeList)
    - 運営元：Alibaba（中国）
    - 電子商取引に関するコンペが多いプラットフォームである
  - [Analytics Vidhya](https://datahack.analyticsvidhya.com/)
    - 運営元：Analytics Vidhya（インド）
    - 目立った賞金はなく、自分の技術力を試す・学習する・純粋に楽しむためのプラットフォームである

## 気になった論文
  - [Deep Neural Networks and Tabular Data: A Survey](https://arxiv.org/pdf/2110.01889.pdf)
    - XGBoost is All You Need.
  - [State-of-the-Art in the Architecture, Methods and Applications of StyleGAN](https://arxiv.org/abs/2202.14020)
    - StyleGANの基礎、問題点、応用を幅広く説明している論文。StyleGAN の潜在空間は非常に強力で、応用すれば年齢や髪型、ポーズなどをリアルに変更したり、有名人や魔法使いなどに変身したりなどの編集ができたり、微調整することで segmentation などのタスクをこなせたりする。
  - [A Tutorial on Distance Metric Learning: Mathematical Foundations, Algorithms, Experimental Analysis, Prospects and Challenges (with Appendices on Mathematical Background and Detailed Algorithms Explanation)](https://arxiv.org/abs/1812.05944)
    - metric learningに関するチュートリアル。

## 学会資料
  - [2022.2.11 第6回 統計・機械学習若手シンポジウム チュートリアル講演 Vision and LanguageとTransformers](https://speakerdeck.com/sei88888/2022-dot-2-11-di-6hui-tong-ji-ji-jie-xue-xi-ruo-shou-sinpoziumu-tiyutoriarujiang-yan-vision-and-languagetotransformers)
    - Twitterで発見。元ツイは[コレ](https://twitter.com/sei_shinagawa/status/1492682815007502336)

## 気になるライブラリ
  - [NeuralForecast](https://nixtla.github.io/neuralforecast/)
    - Twitterで発見。元ツイは[コレ](https://twitter.com/Rami_Krispin/status/1505898362519777287)
  - [trevismd/statannotations](https://github.com/trevismd/statannotations)
    - seabornに統計的有意性の注釈を付与するライブラリ