#LAB 4-2 + Challenge 4.6

age = int(input("나이를 입력하시오: "))
if age >= 15:
    print("본 영화를 보실 수 있습니다.")
    print("영화의 가격은 10000원입니다.")
else:
    print("본 영화를 보실 수 없습니다.")
    print("다른 영화를 보시겠어요?")

cardtype = input("청소년 또는 성인 입력")
if cardtype == "청소년":
    print("청소년입니다.")
else:
    print("승인되었습니다.")