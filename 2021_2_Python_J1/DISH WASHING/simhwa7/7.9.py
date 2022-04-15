# 7.9 사용자로부터 두 문자열 A, B를 입력으로 받도록 하자. 그리고 A의 뒷부분과 B의 앞부분을
# 가장 길게 일치시켜 둘을 겹치게 만든 새로운 문자열 C를 만드는 프로그램을 작성하시오.
# 만약 A의 뒷부분과 B의 앞부분이 다르면 B를 A뒤에 바로 붙여야 한다. 다음 예시를 참고하여라.
# 이를 위하여 C = overlap(A, B)와 같이 A, B를 인자로 받아 C로 반환하는 함수 overlap()을 구현하여라.

A = input("A를 입력하세요: ")     # A 입력 받기
B = input("B를 입력하세요: ")     # B 입력 받기
count = 0

if len(A) > len(B):
    cnt = len(B)
else:
    cnt = len(A)
    
for i in range(cnt):
    if A[-1 - i:]==B[:i + 1]:
        count = i  

print(A + B[count + 1:])