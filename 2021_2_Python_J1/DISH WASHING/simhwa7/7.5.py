# 7.5 ('A', 'B', 'C') 튜플과 ('1', '2')을 조합하여 다음과 같은 공연장의 좌석번호를
# 생성하는 프로그램을 작성하여라. 이때 ('1', '2') 대신 정수로 이루어진 튜플 (1, 2)가 있을 경우
# 동일한 결과가 나타나도록 다시 프로그램을 작성하여라.

alpha = ("A", "B", "C")
num1 = ("1", "2")
num2 = (1, 2)
x = []

for i in alpha:
    for j in num1:
        j = str(j)      # num2를 사용해도 형변환을 사용해 출력한다.
        x.append(i + j)     # x에 담는다
print(x)        # x 출력