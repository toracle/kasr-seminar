# 한국종교사회학회 정례발표회

의미연결망 분석
트위터 등의 SNS나 신문기사 등에서 종교 관련 정보들을 수집하는 방법
수집된 정보를 처리하여 분석하는 방법

가나안 교인, 유교 관련된 분석
동성애, 창조과학, 세습 등에 대한 주제도 좋고.
한국인의 유교 성향을 보여줄 수 있는 분석, 목회자들의 유교 성향 분석, 기독교 언론 기사에 나오는 유교 성향, 목회자 설교문에 나타나는 유교 성향 분석
Chinese Value Survey에서 사용하는 40개 유교 관련 단어 사용하여 어떤 단어들이 한국에서 많이 사용되는지 분석


클리앙에서 '교회', '기독교'라는 키워드 검색해서, 본문 및 댓글 분석하기.


## 일반인들의 기독교에 대한 인식

신문기사에서는 종교 관련 정보가 별로 안나오고, 나온다 하더라도 부정적인 뉴스가 나올 것 같다. 
트위터 등의 SNS에서 기독교인들이 기독교 관련된 기사를 쓸 수는 있어도, 기독교인들끼리만 반응할듯.


## 기독교인의 일반 이슈에 대한 인식

일반 신문기사 등에서, '성경', '예수', '교회', '기독교' 등의 단어를 언급하면서 기독교인이 의견을 표명할 수 있을 것 같다. 일반 사회 이슈에 대한 다른 일반인들과 기독교인들의 인식 차이를 볼 수 있겠다.
하지만 또한 많은 moderate한 기독교인들은 기독교적인 어휘를 사용하지 않으면서 간접적으로 기독교인으로서의 의견을 표명하고 있을 수 있겠다.

그보다는, 같은 이슈에 대해 일반 커뮤니티에서의 문헌과 기독교 커뮤니티에서의 문헌을 조사해보는 것도 좋겠다.
갓톡? 같은 커뮤니티의 멘탈리티가 궁금하긴 하다.


## 기독교인의 기독교에 대한 인식

설교문에서 주요 단어 빈도 분석
설교문에서 주요 단어들에 연관되어 사용되는 단어들 추출 (MDS 등으로 시각화)
설교문 주요 단어들을 클러스터링
몇 명의 설교자들간의 클러스터링 결과 비교하여, 텍스트간의 개념 차이 비교


## 문서 소스

복음과 상황 등에 게제된 글들
설교문: 누구의 설교문들을 구할 수 있나?
클리앙 등 일반 커뮤니티
기독교 관련 커뮤니티?

* 설교문

 * 대한예수교 장로회 평안교회 설교문 [link](http://pyeong-an.com/%EC%84%A4%EA%B5%90-%EB%A7%90%EC%94%80-%EC%9B%90%EA%B3%A0/)
 * 높은뜻 연합선교회 설교문 [link](http://www.godswill.or.kr/index.php?mid=media_2003)


## 참고 분석 케이스

Text Mining the Bible with R, Pt. 1
http://emelineliu.com/2016/01/10/bible1/
http://emelineliu.com/2016/03/20/bible2/


Dive Into NLTK, Part X: Play with Word2Vec Models based on NLTK Corpus
http://textminingonline.com/dive-into-nltk-part-x-play-with-word2vec-models-based-on-nltk-corpus


Dive into NLP with Deep Learning, Part I: Getting Started with DL4NLP
http://textminingonline.com/dive-into-nlp-with-deep-learning-part-i-getting-started-with-dl4nlp


word2vec


## Reference

* Word Embedding의 직관적인 이해: Count Vector에서 Word2Vec에 이르기까지 [Source](https://www.nextobe.com/single-post/2017/06/20/Word-Embedding의-직관적인-이해-Count-Vector에서-Word2Vec에-이르기까지)
* 한국어 Word2vec [Source](http://blog.theeluwin.kr/post/146591096133/한국어-word2vec)
* 단어 임베딩과 word2vec [Source](https://datascienceschool.net/view-notebook/6927b0906f884a67b0da9310d3a581ee/)
* Word2Vec으로 문장 분류하기 [Source](https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/)
* 한글 데이터 머신러닝 및 word2vec을 이용한 유사도 분석 [Source](https://www.nextobe.com/single-post/2017/06/28/한글-데이터-머신러닝-및-word2vec을-이용한-유사도-분석)
* models.word2vec - Deep learning with word2vec [Source](https://radimrehurek.com/gensim/models/word2vec.html)
* SciPy Hierarchical Clustering and Dendrogram Tutorial [Source](https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/)
* K Means Clustering Example with Word2Vec in Data Mining or Machine Learning [Source](http://ai.intelligentonlinetools.com/ml/k-means-clustering-example-word2vec/)
* Using Word2Vec and TSNE [Source](https://www.jeffreythompson.org/blog/2017/02/13/using-word2vec-and-tsne/)

## 분석 #1

설교문에 나타난 어휘망 비교

어휘망을 구하는데 사용한 것은 word2vec. 그것을 t-SNE로 2차원 평면으로 차원 축소 후 matplotlib로 시각화함.


# 데이터 개요

## 설교 원고

원고 있음

* 대한예수교장로회 평안교회 [link](http://pyeong-an.com/설교-말씀-원고/)
* 기독교대한감리회 북수원교회 [link](http://buksuwon.org/main/sub.html?pageCode=68)
* 대한예수교장로회 서문로교회 [link](http://www.e-smr.org/bbs/board.html?code=pastor_02&inc=0)
* 대한예수교장로회 시화충현교회 [link](http://www.scch1.kr/main/sub.html?pageCode=8)
* 소망교회: 설교 텍스트 있음. 게시판 구조 약간 다름 (팝업)
* 높은뜻 연합선교회: 설교 텍스트 있음. 게시판 구조 약간 다름 (연도별 게시판 분리)

원고 없음

* 백주년 기념교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 삼일교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 분당우리교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 선한목자교회: 홈페이지 안열림.
* 지구촌교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 온누리교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 산정현교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 영락교회: 동영상, MP3만 있고 설교도 이미지는 있는데 텍스트 원고는 없음.
* 임마누엘교회: 동영상만 있고 설교 텍스트 원고는 없음.
* 동안교회: 동영상, MP3만 있고 설교 텍스트 원고는 없음.
* 주안장로교회: 동영상만 있고 설교 텍스트 원고는 없음.
