# 9.9 위키 백과사전에서 한국과 관련된 단어들을 찾아 아래 그림처럼 워드 클라우드로 표현해보자.
# 이때 한국과 관련된 단어로 자주 등장하지만 중요한 의미를 갖지 않는 'south', 'north', 'korean', 'world', 'country' 등의
# 단어를 제외할 수 있도록 하라.

import wikipedia            # 위키피디아 import
from wordcloud import WordCloud, STOPWORDS          # wordcloud, STOPWORDS import
import matplotlib.pyplot as plt         # 워드클라우드 시각화를 위한 matplotlib import

wiki = wikipedia.page('South Korea')          # 위키피디아에서 한국 페이지를 불러온다.
text = wiki.content         # 위의 위키 페이지의 텍스트를 추출하도록 한다.

s_words = STOPWORDS.union({'south', 'north', 'korean', 'world', 'country'})         # 제외할 단어 STOPWORDS 집합을 만든다
wordcloud = WordCloud(width=2000, height=1500, stopwords=s_words).generate(text)
# 이미지의 가로 세로 크기를 정하고, generate 함수를 불러와 워드 클라우드를 만들 재료가 될 텍스트 데이터를 인자로 넘겨준다.

plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)           # 화면에 이미지를 그려준다.
plt.show()