# 11.3 numpy의 randint() 함수를 사용하여 30개의 (x, y) 좌표쌍을 2차원 ndarray로 생성하여라.
# 이때 x, y값의 범위는 0에서 50사이의 값으로 하여라. 그리고 생성된 좌표를 matplotlib의 산포도 그래프를 사용하여 그림과 같이 출력하여라.

import numpy as np          # randint() 함수 호출을 위해 numpy import
import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

arr = np.random.randint(0, 51, size=(30, 2))        # x, y값 0까지 50 사이의 값으로 2차원 좌표쌍 30개 생성
x, y = arr.T        # 좌표쌍을 전치 시켜 x, y 값에 주입
plt.scatter(x, y, color='blue')     # 산포도 그래프 생성.
plt.show()      # 그래프 출력