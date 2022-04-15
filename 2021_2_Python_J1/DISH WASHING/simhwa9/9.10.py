# 9.10 한국과 관련된 워드 클라우드를 생성하니 일본이 많이 나타난다. 이번에서 한국과 일본에 관련된 단어들 모아서 아래와 같이 화면에 보여 보자.

import wikipedia            # 위키피디아 import
from wordcloud import WordCloud, STOPWORDS          # wordcloud, STOPWORDS import
import matplotlib.pyplot as plt         # 워드클라우드 시각화를 위한 matplotlib import

wiki1 = wikipedia.page('South Korea')          # 위키피디아에서 한국 페이지를 불러온다.
wiki2 = wikipedia.page('Japan')         # 위키피디아에서 일본 페이지를 불러온다..
text = wiki1.content + wiki2.content         # 위의 한국과 일본의 위키 페이지를 병합해 텍스트를 추출하도록 한다.

s_words = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country'})         # 제외할 단어 STOPWORDS 집합을 만든다
wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)
# 이미지의 가로 세로 크기를 정하고, generate 함수를 불러와 워드 클라우드를 만들 재료가 될 텍스트 데이터를 인자로 넘겨준다.

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)           # 화면에 이미지를 그려준다.
plt.show()
