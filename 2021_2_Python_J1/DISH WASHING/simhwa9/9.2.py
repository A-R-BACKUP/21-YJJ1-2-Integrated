# 9.2 다음과 같이 대문자와 소문자로 이루어진 문자열이 입력되면
# 이 문자열에서 소문자만을 먼저 출력한 후 바로 다음에 대문자가 출현하도록 하여라
# 문자열을 입력하시오 : JoKenTive
# 수정된 문자열 : oeniveJKT

a = str(input('문자열을 입력하시오 : '))         # a에 입력 받은 문자열 저장
b = ""          # 아래 조건문을 돌리면서 조건에 맞는 철자를 담을 b 생성
for i in list(a):
    if(i.islower()):            # i번째의 철자가 소문자일 경우
        b += i          # b에 해당 철자를 담는다.
for i in list(a):
    if(i.isupper()):            # i번째의 철자가 대문자일 경우
        b += i          # b에 해당 철자를 담는다.
print(b)            # 모아진 철자를 print한다.