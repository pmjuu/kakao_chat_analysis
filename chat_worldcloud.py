import os
from wordcloud import WordCloud

BASE_DIR = os.path.dirname(__file__)
CHAT_DATA_DIR = os.path.join(BASE_DIR, 'chat_data')

text_pmj = ""

with open(os.path.join(CHAT_DATA_DIR, "2021.05.20.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if ', 박민주 : ' in line:
            text_pmj += line.split(', 박민주 : ')[1].replace('ㅋ','').replace('ㅎ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','')

font_path = 'C:/Windows/Fonts/malgun.ttf'

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text_pmj)
wc.to_file("wordcloud_pmj.png")