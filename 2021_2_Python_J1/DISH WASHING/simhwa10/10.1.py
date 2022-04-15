# 10.1 다음의 밑줄 친 부분을 넘파이 코드로 채우시오. numpy의 arange() 함수를 사용하여 1에서 20까지의 연속된
# 정수값을 가지는 1차원 배열 num_arr을 생성하여라. 이 배열을 역순으로 출력한 다음 이 배열 원소들의 합을 구하여 출력하라.
# 마지막으로 이 배열을 5행 4열의 2차원 배열로 형태를 변경하여라

import numpy as np      # 넘파이 사용을 위한 import

num_arr = np.arange(1,21)       # 1 ~ 20까지의 연속된 정수값을 가지는  1차원 배열 생성
print(num_arr)      # num_arr 출력

print(num_arr[::-1])        # 배열을 역순으로 출력

print("num_arr 내의 모든 원소의 합 : ",sum(num_arr))        # 배열 원소들의 합 구하기

num_arr = num_arr.reshape(5,4)      # 배열을 5행 4열의 2차원 형태로 변경
print(num_arr)      # 변경된 배열을 출력하기