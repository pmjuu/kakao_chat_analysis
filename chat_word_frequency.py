import os

from pandas import DataFrame

BASE_DIR = os.path.dirname(__file__)
CHAT_DATA_DIR = os.path.join(BASE_DIR, 'chat_data')

names = [i for i in input('공백을 구분자로 사용자 이름을 입력해주세요 : ').split()]
words = {key:[] for key in input('공백을 구분자로 빈도를 알고 싶은 단어를 입력해주세요 : ').split()}
for i in words.values(): #최초에 단어 빈도는 0으로 설정하기. 더 짧게 할 수 없나?
    for _ in range(len(names)):
        i.append(0)

with open(os.path.join(CHAT_DATA_DIR, "2021.05.20.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
    for name in names: #첫번째 사용자부터 분석 시작
        for line in lines:
            if ', '+name+' : ' in line: #이름이 한 줄에 포함되어 있다면
                for word in words.keys(): #그 줄에 포함된 단어 빈도 세기
                    if word in line:
                        words[word][names.index(name)] += 1

print(DataFrame(words, index=names))