# 11.5 다음은 동민이네 동물병원에 치료를 받은 개의 종류와 그 크기 데이터이다. 몸통 길이와 높이는 다음과 같이 cm 단위로 기록하였다.
#
# 1) 이 데이터를 그림으로 다음과 같이 표시하여라. 닥스훈트는 빨간색 동그라미, 사모예드는 파란색 세모, 말티즈는 녹색 네모로 표시하여라
#     (수평축은 길이, 수직축은 높이를 나타내도록 하여라)

import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

dacl = [77, 78, 85, 83, 73, 77, 73, 80]     # 닥스훈트 길이
dach = [25, 28, 29, 30, 21, 22, 17, 35]     # 닥스훈트 높이
# 책에서 나오는 그래프 상에서는 닥스훈트 세번째 높이가 19로 나오는 것 같다.

saml = [75, 77, 86, 86, 79, 83, 83, 88]     # 사모예드 길이
samh = [56, 57, 50, 53, 60, 53, 49, 61]     # 사모예드 높이

mall = [34, 38, 38, 41, 30, 37, 41, 35]     # 말티즈 길이
malh = [22, 25, 19, 30, 21, 24, 28, 18]     # 말티즈 높이

fig, ax = plt.subplots(nrows=1, ncols=3)        # 1행에 3열로 그래프 생성

ax[0].scatter(dacl, dach, color='red')      # 0번째 닥스훈트 그래프 생성 및 빨간색 설정
ax[0].set_title("Dachshund size")       # 제목 설정
ax[0].set_xlabel("Length")      # x축 라벨 설정
ax[0].set_ylabel("Height")      # y축 라벨 설정

ax[1].scatter(saml, samh, color='blue', marker='^')      # 1번째 닥스훈트 그래프 생성 및 삼각형, 파란색 마커 설정
ax[1].set_title("Samoyed size")       # 제목 설정
ax[1].set_xlabel("Length")      # x축 라벨 설정
ax[1].set_ylabel("Height")      # y축 라벨 설정

ax[2].scatter(mall, malh, color='green', marker='s')      # 2번째 닥스훈트 그래프 생성 및 초록색, 사각형 마커 설정
ax[2].set_title("Maltese size")       # 제목 설정
ax[2].set_xlabel("Length")      # x축 라벨 설정
ax[2].set_ylabel("Height")      # y축 라벨 설정

plt.show()      # 그래프 출력
