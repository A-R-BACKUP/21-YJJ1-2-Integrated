# 9.4 다음과 같이 길이가 동일한 두 문자열 a, b가 주어질 경우
# 이 두 문자열을 혼합하여 새로운 유형의 문자열 new_str1, new_str2를 생성하여라.
# new_str1은 a의 문자열 다음에 b의 문자열이 나타나도록 하여 섞는 방식이며,
# new_str2는 a의 첫 문자 다음에 b의 마지막 문자, a의 두 번째 문자 다음에 b의 뒤에서 두 번째 문자.... 의 순서대로 섞이는 방식이다
# a = ABCD
# b = 1234
# new_str1 = A1B2C3D4
# new_str2 = A4B3C2D1

a = str(input('a = '))          # 입력된 값을 a에 넣기
b = str(input('b = '))          # 입력된 값을 b에 넣기
new_str1 = (a[0], b[0], a[1], b[1], a[2], b[2], a[3], b[3])          # a의 문자열 다음에 b의 문자열이 나타나도록 하여 섞는다
new_str2 = (a[0], b[3], a[1], b[2], a[2], b[1], a[3], b[0])          # a의 첫 문자 다음에 b의 마지막 문자, a의 두 번째 문자 다음에 b의 뒤에서 두 번째 문자.... 의 순서대로 섞는다.
print('new_str1 = ', ''.join(new_str1))          # 분리된 문자들을 join을 사용하여 합쳐서 출력한다.
print('new_str2 = ', ''.join(new_str2))          # 분리된 문자들을 join을 사용하여 합쳐서 출력한다.