# 2) 이 표를 subplots() 함수를 이용하여 다음과 같이 막대 그래프, 직선 그래프, 산포도 그래프, 수평막대 그래프로 표현하여라.

import matplotlib.pyplot as plt

Month = [7, 8, 9, 10, 11, 12]           # 월 입력
User = [456, 492, 578, 599, 670, 854]           # 신규 사용자 수 입력

fig, ax = plt.subplots(nrows=1, ncols=4)        # 1행에 4열로 그래프 생성
ax[0].bar(Month, User, color='blue')        # 0번째 막대 그래프 생성
ax[0].set_title("Bar chart")            # 제목 입력
ax[0].xaxis.set_ticks([8, 10, 12])      # 책에 x축 틱이 8, 10, 12만 있으므로 틱 설정
ax[1].plot(Month, User, color='blue', linestyle='solid')        # 1번째 직선 그래프 생성
ax[1].set_title("Line chart")            # 제목 입력
ax[2].scatter(Month, User, color='blue', marker='^')        # 2번째 산포도 그래프 생성, 마커는 삼각형으로
ax[2].set_title("Scatter chart")            # 제목 입력
ax[3].barh(Month, User, color='blue')           # 3번째 수평 막대 그래프 생성
ax[3].set_title("Horizontal Bar chart")            # 제목 입력
plt.show()          # 그래프 띄우기.