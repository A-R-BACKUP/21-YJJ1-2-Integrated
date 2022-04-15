# 11.2 넘파이의 sin(), cos() 함수를 호출하여 그림과 같은 주기할수를 표현해 보자.
# sin(), cos() 등의 삼각함수는 그 주기가 2π이므로 (2 * np.pi) * 6을 통해 6번 반복되는 주기함수를 얻을 수 있다.
# 이 코드에서 sin() 함수는 빨간색 점선으로 표시되는데, x값이 커질수록 y의 진폭이 커지도록 하여라.
# cos() 함수는 파란색 점선으로 나타나 있는데, 출력값은 -1에서 1사이이므로 이 값에 20을 곱하여 -20에서 20사이의 진폭을 가지도록 하여라.

import numpy as np          # sin, cos 함수 호출을 위해 numpy import
import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

x = np.arange(0, 40, 0.1)           # 0에서 40까지 0.1 간격으로 생성
y1 = x * np.sin(x)          # x값이 커질 수록 y의 진폭이 커지게 했다.
y2 = np.cos(x) * 20         # 20을 곱하여 -20에서 20사이의 진폭을 가지게 했다.

plt.plot(x, y1, color='red', linestyle='solid')     # 설명에서는 빨간 점선이라고 했지만 책의 사진에선 그냥 선이라 linestyle을 solid로 설정했다.
plt.plot(x, y2, color='blue', linestyle='--')       # 파란 점선 설정

plt.show()      # 그래프 출력