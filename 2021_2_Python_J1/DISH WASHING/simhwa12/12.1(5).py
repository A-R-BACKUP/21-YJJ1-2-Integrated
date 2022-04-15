# 12.1 이 장에서 사용한 weather.csv 파일을 판다스를 이용하여 읽고 데이터프레임을 만들어 다음과 같은 일을 처리해보자
#
# 5) 울릉도의 평균기온은 30도를 넘는 날들을 찾아, 이날의 기상 데이터를 나열해 보라.

import pandas as pd # pandas 사용을 위해 import

weather=pd.read_csv('./weather.csv',index_col=0,encoding='CP949') # pandas로 csv파일을 읽어옴

print(weather[weather['평균기온']>30]) # 평균기온 열에서 30도를 넘는 것을 찾고 해당되는 열 전체 출력