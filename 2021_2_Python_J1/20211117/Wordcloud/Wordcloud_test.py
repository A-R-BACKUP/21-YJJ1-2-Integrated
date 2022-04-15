from wordcloud import WordCloud, STOPWORDS
s_words = STOPWORDS.union( {'one', 'using', 'first', 'two', 'make', 'use'} )
wordcloud = WordCloud(width = 2000, height = 1500, stopwords = s_words).generate(text)