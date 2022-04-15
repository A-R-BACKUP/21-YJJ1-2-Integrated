# 10.3
# 3) a 배열에서 가장 큰 값이 몇 번째 있는지 구하여 다음과 같이 출력하여라

import numpy as np      # 넘파이 사용을 위한 import
a = np.random.rand(3,3,3)     # 난수로 이루어진 3x3x3 형태의 배열 a생성
print('a의 원소들 중 최댓값의 위치', np.ndarray.argmax(a))
# a 배열에서 가장 큰 값이 몇 번째에 있는지 구하여 출력하기