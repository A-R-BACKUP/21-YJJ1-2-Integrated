# 9.5 다음과 같은 문자열 s가 있다. 이 문자열에는 Korea가 몇 번 나타나는가를 조사하여 출력하라.
# 이때 KOREA, Korea와 korea는 같은 문자열로 간주한다.
# s = Korea is awesome! I REALLY LOVE KOREA.
# Korea의 출현 횟수 : 2

s = 'Korea is awesome! I REALLY LOVE KOREA.'

a = (s.count('Korea'))          # Korea의 개수 카운트
b = (s.count('korea'))          # korea의 개수 카운트
c = (s.count('KOREA'))          # KOREA의 개수 카운트

print('s = Korea is awesome! I REALLY LOVE KOREA.')
print('Korea의 출현 횟수 : ', a + b + c)         # a, b, c의 값 모두 합쳐 출력하기.