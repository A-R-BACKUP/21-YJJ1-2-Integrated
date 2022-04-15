# 7.7 fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']
# 의 리스트가 존재한다

# 1) 이 fruit.list에서 가장 길이가 긴 문자열을 찾아서 출력하고 이 리스트에서 삭제하라.
# 이때 동일한 길이의 문자열이 있을 경우 이들을 모두 삭제하라.

max = 0
max_list = []
fruit = ['banana', 'orange', 'kiwi', 'apple', 'melon']

for i in fruit:
    if len(i)>max:
        max = len(i) # fruit 안에있는것들을 하나씩 비교하며 길이가 가장 긴것을 저장.
print("가장 길이가 긴 문자열: ",end="")
for i in range(len(fruit)):
    if len(fruit[i])==max:
        print(fruit[i],end=" ")
        max_list.append(i) #길이가 가장 긴것들을 모아서 max_list 에 추가
print()
for i in range(len(max_list)):
    fruit.remove(fruit[max_list[-i-1]])
print(fruit) #fruit 에서 길이가 가장 긴 단어들 삭제