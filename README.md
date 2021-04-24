# SCU 雲端運算 X 金融科技
### 課程資訊
2021 東吳大學 巨量資料管理學系課程

學習 AWS 雲端運算服務，共有六次實作作業，包含網頁部署、資料庫服務與建構 Chatbot 等。此外，將會跨校組隊，解決金融業者（如：國泰金控、中信金控、KPMG 等公司）所提供的實務問題。（組隊任務將另開一個 Repo）

* [課程計畫表](http://doc.sys.scu.edu.tw/teachplanHtml/1092/1092MDM65001.html)

授課老師：
蔡芸琤

課程助教：
1. 司福民
2. 陳偉傑
3. 蔡雨臻


### 自我介紹
江祐宏 Alex 

東吳大學-財務工程與精算數學系大四。熱愛探索、挑戰、創新的夢想主義者，不斷地在追求不平凡的人生意義；熱衷於保險科技、程式理財與金融創新；目前是一個不務正業的準財務工程所碩士生。

* [CV_更新至202103](CV_江祐宏.pdf)
* [My_Blog](https://atigerhh880208.medium.com/)

### 內容說明

1. 課堂教材
2. 上課筆記
3. 作業繳交

---
## 作業區
### 作業一
* [HW1](作業繳交/HW1/HW1.md)

### 作業二
* [HW2](https://youtu.be/S7PzpCE3wF8)

### 作業三
* [HW3](https://youtu.be/0ervr1afPbM)

### 作業四
* [HW4](https://youtu.be/-eHEsRW3D-k)

### 作業五

### 作業六

---
## 上課內容
### Week 1~3
* [課程介紹](https://docs.google.com/presentation/d/e/2PACX-1vQQ4-146uvQCZn9VjZKTZM2P_svSrkrzvVN2dlKmXVK3IlqYWTTmBfaG1unOBZ65gOuVyac4c__RIj2/pub?start=false&loop=false&delayms=3000&fbclid=IwAR3B47fq5aXUh_oa6KUf2rF3MyEMeNgh7AU6a_uF2i1gYdL40TOSx06EHtM&slide=id.gbde736d55e_0_107)

* [老師說明專案](https://docs.google.com/presentation/d/1X4xUq4O2z27M1i6cqEV-dBdGyW9aj7nUyFNspkVuF_0/edit#slide=id.gbde736d55e_0_107)

* [六次作業說明](課堂資料/Week_1-3/20210221_Cloud-Computing_Introduction.pptx)

* [AWS簡介](課堂資料/Week_1-3/20210221_Cloud_Computing_Fields.pptx)

Note:
1. 雲端運算的部署方法指的是：「誰擁有使用權限」
2. 在傳統的伺服器架構，假設只有一台電腦，會有「單點故障問題」，一台壞掉了，就沒有辦法繼續運作了。因此，會進行伺服器擴充，擴充後資料必須要先傳到擁有附載平衡器的伺服器裡，再分散給其他伺服器。然而，誰要當附載平衡？怎麼分配給不同的伺服器？只有一台附載平衡也同樣會有單點故障的問題？雲端運算的出現解決了傳統伺服器的痛點。
3. 起初 Amazon 在做電商時，因為特殊節慶造成消費者流量大增而買入大量主機，但平常這些主機閒置著反而造成了資源浪費，因此 Amazon 開始嘗試，用網際網路來分享這些閒置的伺服器空間，就是雲端運算的起源。

### Week 4
* [老師說明專案](https://docs.google.com/presentation/d/e/2PACX-1vTgVktGm1OwqWspx_PkFQlhR6oqPFXTV5oj0JYOdR-guBzKBEbyXLfKKXRenI2HkhT4iHwYGStgoAIA/pub?start=false&loop=false&delayms=3000&slide=id.gc356cb2501_0_119)

* [AWS EC2簡介](課堂資料/Week_4/EC2_with_LAMP.pptx)

### Week 5
* [老師說明專案](https://docs.google.com/presentation/d/1-FBkCGspeQP25hUPDf7VRT7mN50Fn5uBvBH7vI-GDkY/edit#slide=id.gbde736d55e_0_107)

* [AWS S3簡介](課堂資料/Week_5/S3_Static_Web_Hosting.pptx)

### Week6~7
* [老師說明專案](https://docs.google.com/presentation/d/1IsY6-iJ85igRFtwcVSprsv0J_dPTxUisQaOCmDKxfrs/edit#slide=id.gbde736d55e_0_107)

* [AWS API Gateway 與 Lambda簡介](課堂資料/Week_6-7/20210329_API_Gateway_Lambda_Chatbot.pptx)

### Week 8~9
* [老師說明專案](https://docs.google.com/presentation/d/1lKEjVD89RqyJKzTYhfanL6EdN6AHLfiodcv9jbqLxK0/edit#slide=id.gbde736d55e_0_107)

* [AWS RDS 與 DynamoDB 簡介](課堂資料/Week_8~10/RDS_DynamoDB_CRUD.pptx)

* [AWS RDS 與 DynamoDB 程式實作](課堂資料/Week_8~10/Cloud_Computing_Database_Services.ipynb)


### Week 10
* [Docker 簡介](https://www.notion.so/Docker-5cc2ffdbebd44dc1ab46ab1dfc31ebeb)

* [Docker 補充資料 1](https://philipzheng.gitbook.io/docker_practice/)

* [Docker 補充資料 2](https://tw.alphacamp.co/blog/docker-introduction)

* [Docker 補充資料 3](https://cwhu.medium.com/docker-tutorial-101-c3808b899ac6)

* [Docker 補充資料 4](https://github.com/komavideo/LearnDocker)

Note:
『虛擬機』是以作業系統為核心，將主機做分割；而 Docker 就像『輕量級的虛擬機』，以應用程式(包含 code, 執行環境)為核心將其虛擬化

[Dockerfile] --> build --> [Image] --> run --> [Container] --> store --> [Repository]

1. Dockerfile
> 撰寫打包方式、基礎設置

2. Image
> * Read-only
> * 可堆疊
> * code + 函式庫 + SQL + 作業系統 + ...... （包裝好的物件）

3. Container
> * 實際執行的應用
> 設置: (1)Network 對外通訊 (2)Volume 共享資料

4. Repository
> Docker Hub，類似於 Git hub，執行 pull, push 當中的 Image

### Week 11
* [助教說明專案](https://docs.google.com/presentation/d/e/2PACX-1vR6RshhTnxcEtebBKObOhpKNpoioxb8O3zNBlVpx6BNYX8tFN-MYQJeA9lGRgNnirDL9Ciwi1odpinD/pub?start=false&loop=false&delayms=3000&slide=id.p)

