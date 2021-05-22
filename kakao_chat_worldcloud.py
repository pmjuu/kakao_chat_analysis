from wordcloud import WordCloud

text_pmj = ""
text_les = ""

with open("C:/1Python test/카톡.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if ', 박민주 : ' in line:
            text_pmj += line.split(', 박민주 : ')[1].replace('ㅋ','').replace('ㅎ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','')
        if ', 이은섭 : ' in line:
            text_les += line.split(', 이은섭 : ')[1].replace('ㅋ','').replace('ㅎ','').replace('ㅠ','').replace('ㅜ','').replace('사진\n','').replace('이모티콘\n','')

# import matplotlib.font_manager as fm
#
# for font in fm.fontManager.ttflist:
#  if 'Gothic' in font.name:
#    print(font.name, font.fname)

font_path = 'C:/Windows/Fonts/malgun.ttf'

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
wc.generate(text_pmj)
wc.to_file("wordcloud_pmj.png")
wc.generate(text_les)
wc.to_file("wordcloud_les.png")