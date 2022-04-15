# 10.2 다음 각각의 문제들을 넘파이를 활용하여 해결해 보라.
# 1) 다음과 같이 0에서 24까지의 값을 가지는 5x5 크기의 2차원 행렬 n_arr을 생성하여라.

import numpy as np      # 넘파이 사용을 위한 import

n_arr = np.arange(0,25)     # 먼저 0부터 24까지의 값을 가지는 배열 생성
n_arr = n_arr.reshape(5,5)      # 생성된 배열을 5x5 크기로 변경하기
print(n_arr)        # 생성된 배열을 출력하기