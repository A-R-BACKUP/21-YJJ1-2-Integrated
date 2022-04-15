# 12.3 다음은 Q 자동차 회사의 차종별 마력, 총중량, 그리고 연비를 나타낸 표이다.
#
# 3) 각 차량의 제조사를 알 수 있게 다음과 같이 데이터프레임을 다시 만들어 보라.

import pandas as pd # pandas 사용을 위해 import

P = pd.DataFrame({'name' : ['A','B','C','D','E','F','G'],
                  'horse power':[130,250,190,300,210,220,170],
                  'weight':[1.9,2.6,2.2,2.9,2.4,2.3,2.2],
                  'efficiency':[16.3,10.2,11.1,7.1,12.1,13.2,14.2]})
# P 데이터프레임 생성
Q = pd.DataFrame({'name' : ['A','B','C','D'],
                  'horse power':[120,220,120,200],
                  'weight':[1.9,2.1,1.5,2.9],
                  'efficiency':[18.3,19.2,21.1,17.3]})
# Q 데이터프레임 생성
# 책에 있는 표에서는 총 즁량이 kg 단위로 나오는 것으로 보이나 책에 있는 결과값은 t 단위로 출력하고 있어 t 단위로 수정함.

P['com']='P' # P에 com 열 생성
Q['com']='Q' # Q에 com 열 생성

print(pd.concat([P,Q]).set_index('name'))
# .concat([P,Q])를 사용하여 P 데이터와 Q 데이터를 합친 후 name을 인덱스로 하여 출력