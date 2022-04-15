# 12.1 이 장에서 사용한 weather.csv 파일을 판다스를 이용하여 읽고 데이터프레임을 만들어 다음과 같은 일을 처리해보자
#
# 4) 가장 무더웠던 날이 언제이고, 이 날의 평균기온, 평균 풍속, 최대풍속을 알아 보라

import pandas as pd # pandas 사용을 위해 import

weather=pd.read_csv('./weather.csv',index_col=0,encoding='CP949') # pandas로 csv파일을 읽어옴

print(weather[weather['평균기온']==weather['평균기온'].max()]) # 평균기온 열에서 최댓값을 찾고 해당되는 행 전체 출력