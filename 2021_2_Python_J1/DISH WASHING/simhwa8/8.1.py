# 8.1) 철수네 과일가게는 "사과", "배", "수박", "귤", "포도"를 판매하는 중이다.
# 매일 매일 입고되는 가격에 따라서 가격이 결정되므로 아침마다 각 과일의 가격을 입력하는 기능을 만들어서
# 입력하면 이를 출력하여 다음과 같이 표시하고자 한다.
# 이와 같은 기능을 수행하는 파이썬 프로그램을 작성하여라.
# 이때 ('사과' : 3000)과 같이 입련된 키 값을 키-값의 쌍으로 된 fruits_price 딕셔너리에 추가한 후
# for 문과 keys() 메소드를 사용하여 출력하도록 하여라.

while True:
    a=[]
    fruit_price = {'사과':0,'배':0,'수박':0,'귤':0,'포도':0}        #각 과일의 변수 생성

    a=input("사과, 배, 수박, 귤, 포도 가격을 공백으로 구분하여 입력(종료를 원하면 -1 입력) : ").split(' ')
    # 가격 물어보기


    print(a)
    if a[0]=='-1':
        print('실행 종료') # -1을 입력 받으면 실행 종료하게 한다.
        break

    print('------ 오늘의 과일 가격 ------')
    i = 0
    for key in fruit_price.keys():      # 반복문을 사용하여 가격 주입하며 결과 출력
        fruit_price[key]=a[i]
        print(key+" : "+fruit_price[key])
        i += 1