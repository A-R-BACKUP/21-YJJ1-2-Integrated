# 12.2 다음은 P 자동차 회사의 차종별 마력, 총중량, 그리고 연비를 나타낸 표이다.
#
# 3) 마력과 연비를 곱한 값이 가장 큰 차종을 다음과 같이 찾아 보라

import pandas as pd # pandas 사용을 위해 import

P = pd.DataFrame({'name' : ['A','B','C','D','E','F','G'],
                  'horse power':[130,250,190,300,210,220,170],
                  'weight':[1.9,2.6,2.2,2.9,2.4,2.3,2.2],
                  'efficiency':[16.3,10.2,11.1,7.1,12.1,13.2,14.2]})
# 판다스 데이터프레임 생성

P['hp x mile'] = P['horse power'] * P['efficiency']
print(P[P['hp x mile']==P['hp x mile'].max()].set_index('name'))
# 마력과 연비를 곱한 값 중에서 최댓값을 name을 인덱스로 하여 출력