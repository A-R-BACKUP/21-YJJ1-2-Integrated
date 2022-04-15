# 11.1 대한 컴퍼니의 영업 1부에 근무하는 강이안씨는 초고속 인터넷 가입형 상품 "빠르다넷(speeda net)"의 가입 영업을 하고 있다.
# 강이안씨의 영업은 성공적으로 이루어져서 매달 새로운 사용자가 꾸준히 가입하고 있으며 이를 보여주기 위해, 다음 표와 같은 회사의 신규 사용자 통계자료를 준비했다.
#
#    월        7월      8월      9월      10월     11월     12월
# 신규 사용자    456     492      578      599     670     854
#
# 1) 이 표를 바탕으로 다음과 같은 차트를 그려보아라.

import matplotlib.pyplot as plt         # 차트를 그리기 위한 matplotlib import

Month = [7, 8, 9, 10, 11, 12]           # 월 입력
User = [456, 492, 578, 599, 670, 854]           # 신규 사용자 수 입력

plt.plot(Month, User, color='blue', linestyle='solid')      # x축에 월, y축에 신규 사용자 직선으로 띄운다.
plt.title("Daehan company speeda net new costomers")        # 제목 띄우기

plt.xlabel("Month")         # x축 라벨
plt.ylabel("User")          # y축 라벨
plt.show()          # 차트 띄우기