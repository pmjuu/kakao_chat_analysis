import os
import re
from pandas import DataFrame

BASE_DIR = os.path.dirname(__file__)
CHAT_DATA_DIR = os.path.join(BASE_DIR, 'chat_data')

words = ['ㅎ', '번째']
# words = input('공백을 구분자로 빈도를 알고 싶은 단어를 입력해주세요 : ').split()
wordTable = {key:[] for key in words}

with open(os.path.join(CHAT_DATA_DIR, "test.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()[2:]
    #데이터 정제하기
    lines = [line.rstrip() for line in lines if line != '\n'] #개행문자와 빈 줄 삭제
    for line in lines: #년월일 삭제
        m = re.match('\d+년 \d+월 \d+일 \D요일', line)
        if m:
            print('년월일 삭제:', line)
            lines.remove(line)

    for line in lines: #줄바꿈된 문장 하나로 합치기
        m = re.match('\d+. \d+. \d+. 오\D \d+:\d+, ', line)
        if not m:
            print('메시지 내 줄바꿈 감지:', line)
            n = lines.index(line)
            lines[n-1] += (' '+line)  #이전 line에 현재 line 합치고
            lines.remove(line) #현재 line 삭제

    print(lines)
    with open(os.path.join(CHAT_DATA_DIR, "test_data_refine.txt"), "w", encoding="utf-8") as fw: #정제된 데이터txt파일
        for line in lines:
            fw.write(line+'\n')

    names = sorted({line[(line.find(',')+2):(line.find(' :'))] for line in lines if ', ' in line and ' : ' in line}) #', '과 ' :' 사이에 있는 사용자 이름 모으기. set으로 중복제거하고 정렬된 리스트로 변환
    sentencesList = [[line for line in lines if ', '+name+' : ' in line] for name in names] #사용자 별로 문장 분류. ex)첫번째 요소는 사용자1의 문장들

    for sentences in sentencesList: #사용자1 문장들 부터 분석 시작
        for word in words:
            temp = 0
            for sentence in sentences:
                temp += sentence.count(word)
            wordTable[word].append(temp)

print('='*3, '단어 빈도 분석 결과', '='*3)
print(DataFrame(wordTable, index=names))
print('='*7, '총 대화 수', '='*7)
for i in range(len(names)): #사용자 별로 대화 개수 출력
    number = len(sentencesList[i])
    print(names[i], ':', number, '개')

