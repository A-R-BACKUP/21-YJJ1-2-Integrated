#LAB 3-3
sex = int(input("남성이면 0, 여성이면 1을 입력하시오.: "))
weight = float(input("몸무게를 kg 단위로 입력하시오.: "))
height = float(input("키를 cm 단위로 입력하시오.: "))
ro = float(input("허리둘레를 입력하시오.: "))
bmi = (weight / ((height / 100) ** 2))
print("당신의 BMI = ", bmi)
if sex == 0:
    rfmm = 64 - (20 * (height / ro))
    print("당신의 RFM: ", rfmm)
if sex == 1:
    rfmw = 76 - (20 * (height / ro))
    print("당신의 RFM: ", rfmw)