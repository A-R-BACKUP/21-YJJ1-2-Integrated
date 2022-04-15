# 10.3
# 2) a 배열에서 가장 큰 값을 구하여 다음과 같이 출력하여라

import numpy as np      # 넘파이 사용을 위한 import
a = np.random.rand(3,3,3)     # 난수로 이루어진 3x3x3 형태의 배열 a생성
print('a의 원소들 중 최댓값 : ', np.ndarray.max(a))        # a 배열에서 가장 큰 값을 구해서 출력