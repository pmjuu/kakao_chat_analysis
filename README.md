# 카톡대화 분석
모바일 카카오톡에서 텍스트 내보내기한 txt파일을 바탕으로 내용 분석하기
<br>
## 단어 빈도 구하기
[단어 빈도 구하기.py](./chat_word_frequency.py)   

### 활용된 문법
[정규표현식](https://wikidocs.net/4308)

<br>
## 워드클라우드
[WordCloud.py](./chat_worldcloud.py)
### wordcloud 패키지 설치하기   
`pip install -r requirements.txt`<br>   

### 오류일지   
module 'sip' has no attribute 'setapi' 오류 뜸 -> C:\Anaconda3\Library\bin>pip install matplotlib==3.2   
There seems to be an incompatibility issue using Matplotlib version 3.3 with IPython. For now, you can fix it by installing Matplotlib 3.2.   
출처: stack overflow <br>   

### 후기
그림으로 보는 것말고 수치를 보여주는 시각화 툴을 이용하는게 알아보기 쉽겠다.   
그림 형태는 그냥 시각적 재미로 보기에 좋은 것 같다.
