# 7.2 다음과 같은 list1, list2가 있을 경우 이중 for 루프를 사용하여 list1과 list2의
# 각 원소를 곱한 후 원소의 곱셈을 아래와 같이 출력하시오.

list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]


for i in list1:        # 리스트1을 하나씩 i에 대입
    for j in list2:     # 리스트2를 하나씩 j에 대입
        print(i, "*", j, " = ", i * j)       # i * j 곱한 값을 출력