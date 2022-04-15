# 12.1 이 장에서 사용한 weather.csv 파일을 판다스를 이용하여 읽고 데이터프레임을 만들어 다음과 같은 일을 처리해보자
#
# 3) 이 데이터에 기록된 날들 중에서 가장 무더웠던 날의 평균 기온은 얼마였는지 찾아보라

import pandas as pd # pandas 사용을 위해 import

weather=pd.read_csv('./weather.csv',index_col=0,encoding='CP949') # pandas로 csv파일을 읽어옴

print(weather['평균기온'].max()) # 평균기온의 열 중에서 최댓값 출력