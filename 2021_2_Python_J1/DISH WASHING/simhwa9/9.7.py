# 9.7 카이사르의 암호 문장을 만드는 문제를 조금 수정하여 대문자, 소문자를 가리지 않고 암호문을 만드는 프로그램을 만들어보자.
# 물론 문자를 제외한 숫자나 특수문자는 암호화를 하지 않도록 하자. 다음과 같이 사용자로부터 문장과 함께 이동시킬 칸 수를 입력 받아서 암호문을 생성하도록 하자.
#
# 문장을 입력하시오 : Veni, vidi, vici.
# 이동시킬 칸 수를 입력하시오 : 3
# 암호화된 문장 : Yhql, ylgl, ylfl.

import string

src = str(input('문장을 입력하시오 : '))            # 문장을 입력 받아 src에 주입
i = int(input('이동시킬 칸 수를 입력하시오 : '))            # 이동 시킬 칸수를 입력 받아 i에 주입
print('암호화된 문장 : ', end='')         # 암호화 된 문장을 출력


src_str = string.ascii_uppercase + string.ascii_lowercase           # String 모듈의 아스키 대문자열과 소문자열을 불러와 합친다
dst_str = src_str[i:] + src_str[:i]         # i칸 만큼 문자열을 밀어낸 문자열을 만든다

def cipher(a):          # ciper 함수를 만든다.
    idx = src_str.index(a)          # cipher(a)는 src_str 안에서 a 라는 문자를 가진 곳의 index를 찾아서
    return dst_str[idx]         # 그 index를 dst_str[index] 에 넣어서 문자 하나를 리턴

for ch in src:
    if ch in src_str:
        print(cipher(ch), end='')
    else:
        print(ch, end='')

print()
# src배열의 문자 하나하나 ch 로 반복문 돌리면서 ch가 src_str 안에 있으면 cipher함수로 반환한 값을 출력
#
# 아니면 (숫자, 특수문자) 그냥 출력