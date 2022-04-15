# 9.1 다음과 같이 3단어로 된 영문 이름을 입력 받은 후 중간 이름을 출력하여라
# 이름을 입력하시오 : John Fitzgerald Kennedy
# 중간 이름은 : Fitzgerald

a = str(input('이름을 입력하시오 : '))      # a에 이름 입력 받기
b = a.split()       # 이름 split 후 b에 저장하기
print(b[1])         # split 된 부분의 1번째 출력하기


