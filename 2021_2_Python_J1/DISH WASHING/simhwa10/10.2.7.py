# 10.2 다음 각각의 문제들을 넘파이를 활용하여 해결해 보라.
# 7) n_arr 배열에 슬라이싱을 적용하여 다음과 같은 값을 가지는 배열을 생성하여라.

import numpy as np      # 넘파이 사용을 위한 import

n_arr = np.arange(0,25)     # 먼저 0부터 24까지의 값을 가지는 배열 생성
n_arr = n_arr.reshape(5,5)      # 생성된 배열을 5x5 크기로 변경하기
n_arr = n_arr[0:2]       # 0~1행 출력하기
n_arr=n_arr.reshape(5,2)        # 5행 2열 배열로 변경하기
print(n_arr)        # n_arr 출력하기
