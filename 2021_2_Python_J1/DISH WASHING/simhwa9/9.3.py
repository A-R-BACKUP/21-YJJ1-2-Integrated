# 9.3 다음과 같이 대문자와 소문자, 특수문자, 숫자로 이루어진 문자열이 입력되면,
# 각각의 출현 횟수를 출력하는 코드를 작성하여라.
# 문자열을 입력하시오 : JoP&*()193at25^^
# 대문자, 소문자, 숫자, 특수문자의 개수
# 대문자 = 2
# 소문자 = 3
# 숫자 = 5
# 특수문자 = 6

a = str(input('문자열을 입력하시오 : '))         # 문자열 입력 받기
up = sum(i.isupper() for i in a)            # 대문자 찾아내서 개수 합하기
lw = sum(i.islower() for i in a)            # 소문자 찾아내서 개수 합하기
nm = sum(i.isdigit() for i in a)            # 숫자 찾아내서 개수 합하기
sc = sum(i.isalnum() for i in a)            # 영문과 숫자 찾아내서 개수 합하기
print('대문자, 소문자, 숫자, 특수문자의 개수')
print('대문자 = ', up)            # 대문자 개수 출력하기
print('소문자 = ', lw)            # 소문자 개수 출력하기
print('숫자 = ', nm)            # 숫자 개수 출력하기
print('특수문자 = ', len(a) - sc)            # 전체 문자 개수에서 영문과 숫자 개수 뺀 결과 출력하기.