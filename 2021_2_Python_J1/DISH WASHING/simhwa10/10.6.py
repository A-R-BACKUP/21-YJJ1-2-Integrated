# 10.6 다음과 같이 나타나는 4개의 리스트 데이터가 있다.
# 이 리스트 데이터의 상관관계를 구하여 다음과 같은 표로 나타내어라.

import numpy as np
x1 = [i for i in range(100)]            
x2 = [i+np.random.randint(1,10) for i in range(100)]
x3 = [i+np.random.randint(1,50) for i in range(100)]
x4 = [np.random.randint(1,10) for i in range(100)]
# 책에서 나온 배열 생성

result =np.corrcoef([x1,x2,x3,x4]) # .corrcoef 함수를 이용해 상관관계 계산하기
print(result)       # 출력하기

