# 11.5 다음은 동민이네 동물병원에 치료를 받은 개의 종류와 그 크기 데이터이다. 몸통 길이와 높이는 다음과 같이 cm 단위로 기록하였다.
#
# 2) 이 세 종류의 개들이 한 화면에 나타나도록 하여라. 이때 다음과 같이 범례가 함께 나타나도록 하여라.

import matplotlib.pyplot as plt         # 그래프 작성을 위한 matplotlib import

dacl = [77, 78, 85, 83, 73, 77, 73, 80]     # 닥스훈트 길이
dach = [25, 28, 29, 30, 21, 22, 17, 35]     # 닥스훈트 높이
# 책에서 나오는 그래프 상에서는 닥스훈트 세번째 높이가 19로 나오는 것 같다.

saml = [75, 77, 86, 86, 79, 83, 83, 88]     # 사모예드 길이
samh = [56, 57, 50, 53, 60, 53, 49, 61]     # 사모예드 높이

mall = [34, 38, 38, 41, 30, 37, 41, 35]     # 말티즈 길이
malh = [22, 25, 19, 30, 21, 24, 28, 18]     # 말티즈 높이

plt.scatter(dacl, dach, color='red', label='Dachshund')     # 닥스훈트 그래프 생성 및 라벨 생성
plt.scatter(saml, samh, color='blue', marker='^', label='Samoyed')      # 사모예드 그래프 생성 및 라벨 생성
plt.scatter(mall, malh, color='green', marker='s', label='Maltese')     # 말티즈 그래프 생성 및 라벨 생성
plt.title("Dog size")       # 제목 생성
plt.xlabel("Length")        # x축 라벨 생성
plt.ylabel("Heigth")        # y축 라벨 생성
plt.legend(loc='upper left')        # 범례 위치 왼쪽 상단으로 수정
plt.show()      # 그래프 출력