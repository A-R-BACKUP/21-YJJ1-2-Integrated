# 7.3 다음과 같은 문자열을 가진 두 개의 리스트 list1, list2가 있을 경우
# list1과 list2의 모든 조합을 생성하여 다음과 같이 출력하시오.

list1= ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']

for i in list1:     # 문자열 한개씩 대입
    for j in list2:
        print(i + " " + j)