# 8.2) 8.1번 문제에서 입력받은 fruit_price 딕셔너리의 가격정보를 사용하여 고객이 입력하면 출력하는
# 다음과 같은 프로그램을 작성하여라.

fruit_price = {'사과':'3000','배':'4500','수박':'6000','귤':'2400','포도':'3400'}
# 각 과일의 가격 생성
name = input('구매를 원하는 과일의 이름을 입력하시오 : ')
# 과일 가격 물어보고 name에 넣기
print('오늘의 ',name,'가격은', fruit_price[name],'원 입니다.')
# 과일 가격 출력하기