# 7.4 다음의 코드에서 잘못된 부분은 무엇인가? 어떤 이유에서 오류가 발생하는지 설명하라.

# 1)
t = [10, 20, 30, 40]
t.append(50)        # t에 50 추가
print('(1)', t)

#2)
t = [10, 20, 30, 40]
t.remove(40)        # 3번째 40 값을 제거
print('(2)', t)

# 3)
t = [10, 20, 30, 40]
t[0] = 0      # 0번째 값을 0으로 바꿈
print('(3)', t)
