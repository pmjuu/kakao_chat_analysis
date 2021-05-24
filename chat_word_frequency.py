import os
from pandas import DataFrame

BASE_DIR = os.path.dirname(__file__)
CHAT_DATA_DIR = os.path.join(BASE_DIR, 'chat_data')

words = input('공백을 구분자로 빈도를 알고 싶은 단어를 입력해주세요 : ').split()
wordTable = {key:[] for key in words}

with open(os.path.join(CHAT_DATA_DIR, "2021.05.20.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
    #데이터 정제하기
    lines = lines[2:]

    names = {line[(line.find(',')+2):(line.find(' :'))] for line in lines if ', ' in line and ' : ' in line} #사용자 이름 모으기. set으로 중복제거
    names = list(names)
    names.sort()
    sentencesList = [[line for line in lines if ', '+name+' : ' in line] for name in names] #사용자 별로 문장 분류. ex)첫번째 요소는 사용자1의 문장들

    for sentences in sentencesList: #사용자1 문장들 부터 분석 시작
        for word in words:
            temp = 0
            for sentence in sentences:
                temp += sentence.count(word)
            wordTable[word].append(temp)

print(DataFrame(wordTable, index=names))
print('='*5, '총 대화 수', '='*5)
for i in range(len(names)): #사용자 별로 대화 개수 출력
    number = len(sentencesList[i])
    print(names[i], ':', number, '개')