# 11.4 numpy의 난수생성기를 이용하여 각각 1000개의 난수를 가지는 3가지 종류의 (x, y) 분포를 생성하고 matplotlib의 산포도 그래프로 나타내어라.
# 왼쪽의 그림은 x 값과 y 값이 각각 평균이 25이고 표준편차가 6인 특성을 가진다.
# 가운데 그림을 x 값의 평균이 25이고 표준편차가 6인 특성을 가지며 y 값은 평균이 25이고 표준 편차가 3인 특성을 가진다.
# 가장 오른쪽은 x 값의 평균이 25이고 표준편차가 6인 특성을 가지며 y 값은 x 값에 표준정규분포 난수를 더한 값이다.

import numpy as np          # 난수생성기 호출을 위해 numpy import
import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

fig, ax = plt.subplots(nrows=1, ncols=3)        # 1행에 3열로 그래프 생성

leftxy = 25 + 6 * np.random.randn(1000, 2)       # 평균이 25이고 표준편차가 6인 정규분포를 가지는 좌표쌍 생성
leftX, leftY = leftxy.T     # 좌표쌍을 전치 시켜 leftX, leftY에 주입

ax[0].scatter(leftX, leftY, color='blue')        # 0번째 막대 그래프 생성 및 파란색 설정
ax[0].xaxis.set_ticks([0, 10, 20, 30, 40, 50])      # x축 틱 설정
ax[0].yaxis.set_ticks([0, 10, 20, 30, 40, 50])      # y축 틱 설정



midX = 25 + 6 * np.random.randn(1000, 1)       # 평균이 25이고 표준편차가 6인 정규분포를 가지는 x값 생성
midY = 25 + 3 * np.random.randn(1000, 1)       # 평균이 25이고 표준편차가 3인 정규분포를 가지는 y값 생성

ax[1].scatter(midX, midY, color='red')        # 1번째 막대 그래프 생성 및 빨간색 설정
ax[1].xaxis.set_ticks([0, 10, 20, 30, 40, 50])      # x축 틱 설정
ax[1].yaxis.set_ticks([0, 10, 20, 30, 40, 50])      # y축 틱 설정



rigX = 25 + 6 * np.random.randn(1000, 1)       # 평균이 25이고 표준편차가 6인 정규분포를 가지는 x값 생성
rigY = rigX + np.random.randn(1000, 1)         # x값에 표준정규분포 난수 더하여 y에 주입

ax[2].scatter(rigX, rigY, color='green')        # 2번째 막대 그래프 생성 및 초록색 설정
ax[2].xaxis.set_ticks([0, 10, 20, 30, 40, 50])      # x축 틱 설정
ax[2].yaxis.set_ticks([0, 10, 20, 30, 40, 50])      # y축 틱 설정

plt.show()      # 그래프 출력