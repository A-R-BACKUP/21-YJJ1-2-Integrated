# 12.2 다음은 P 자동차 회사의 차종별 마력, 총중량, 그리고 연비를 나타낸 표이다.
#
# 1) 이 데이터프레임의 name 열을 인덱스로 사용하고 싶다. set_index('name')을 데이터프레임에 적용하여 다음과 같은 결과가 나오게 만들어 보라.

import pandas as pd # pandas 사용을 위해 import

P = pd.DataFrame({'name' : ['A','B','C','D','E','F','G'],
                  'horse power':[130,250,190,300,210,220,170],
                  'weight':[1.9,2.6,2.2,2.9,2.4,2.3,2.2],
                  'efficiency':[16.3,10.2,11.1,7.1,12.1,13.2,14.2]})
# 판다스 데이터프레임 생성

print(P.set_index('name')) # .set_index('name') 를 이용하여 name열을 인덱스로 사용함