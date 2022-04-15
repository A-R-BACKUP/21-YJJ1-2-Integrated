# 12.1 이 장에서 사용한 weather.csv 파일을 판다스를 이용하여 읽고 데이터프레임을 만들어 다음과 같은 일을 처리해보자
#
# 2) 2015년 6월 6일의 울릉도 평균 기온과 풍속 정보를 다음과 같이 확인해 보라.

import pandas as pd # pandas 사용을 위해 import

weather=pd.read_csv('./weather.csv',index_col=0,encoding='CP949') # pandas로 csv파일을 읽어옴

print(weather.loc['2015-06-06']) # weather.csv 에서 2015-06-06의 값을 찾아서 그 행을 출력함