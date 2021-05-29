# 카톡대화 분석
## 단어 빈도 구하기
[단어 빈도 구하기ver1.py](./chat_word_frequency.py)  
### 후기
* ~~특히 이모티콘이 포함된 경우, 사용자 이름을 입력하는게 번거로웠다. 사용자 이름을 자동으로 입력받도록 만들어야겠다.~~
* 데이터 정제가 필요함. 이름 뒤에 오는 문장 속에서 단어 빈도를 구하도록 바꿔야겠다. (ver1은 날짜부터 시작해서 한 문장 안에서 단어 포함 여부를 판단함)
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
