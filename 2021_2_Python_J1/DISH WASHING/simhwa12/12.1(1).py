# 12.1 이 장에서 사용한 weather.csv 파일을 판다스를 이용하여 읽고 데이터프레임을 만들어 다음과 같은 일을 처리해보자
#
# 1) 이 데이터의 앞 3개 행과 마지막 3개 행을 다음처럼 화면에 나타내어라

import pandas as pd # pandas 사용을 위해 import
weather=pd.read_csv('./weather.csv',index_col=0,encoding='CP949') # pandas로 csv파일을 읽어옴

print(weather.head(3)) # .head(3)를 이용해 앞 3개 행 출력
print(weather.tail(3)) # .tail(3)을 이용해 뒤 3개 행 출력