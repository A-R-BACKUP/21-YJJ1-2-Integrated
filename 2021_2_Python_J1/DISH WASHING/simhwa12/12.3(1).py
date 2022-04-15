# 12.3 다음은 Q 자동차 회사의 차종별 마력, 총중량, 그리고 연비를 나타낸 표이다.
#
# 1) 이 표를 판다스 데이터프레임으로 만들어 출력해 보라.

import pandas as pd # pandas 사용을 위해 import
Q = pd.DataFrame({'name' : ['A','B','C','D'],
                  'horse power':[120,220,120,200],
                  'weight':[1.9,2.1,1.5,2.9],
                  'efficiency':[18.3,19.2,21.1,17.3]})
# Q 데이터프레임 생성
# 책에 있는 표에서는 총 즁량이 kg 단위로 나오는 것으로 보이나 책에 있는 결과값은 t 단위로 출력하고 있어 t 단위로 수정함.

print(Q.set_index('name')) # name열을 인덱스로 하여 Q 데이터프레임 출력