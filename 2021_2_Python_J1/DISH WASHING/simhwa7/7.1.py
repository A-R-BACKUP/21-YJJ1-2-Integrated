# 7.1 다음과 같이 파이썬 프로그램을 실행할 적에, 다음 밑줄 안에 들어갈 알맞은 결과는 무엇인가?
# 미리 예측해본 후 실행시켜보고 그 결과를 적으시오.

num_list = [100, 200, 300, 400, 500, 600, 700, 800]
high = 6
low = 3

print('-------------------')
print('num_list[high]')
print(num_list[high])       # (1) list [6]출력
print('-------------------')
print('num_list[high - 2]')
print(num_list[high - 2])     # (2) list [4] 출력
print('-------------------')
print('num_list[high - low]')
print(num_list[high - low])     # (3) list [3] 출력
print('-------------------')
print('num_list[low - high]')
print(num_list[low - high])         # (4) list [-3] 출력
print('-------------------')
print('num_list[-1]')
print(num_list[-1])     # (5) list [-1] 출력
print('-------------------')
print('num_list[-low]')
print(num_list[-low])       # (6) list [-3] 출력
print('-------------------')
print('num_list[2 * 3]')
print(num_list[2 * 3])        # (7) list [6] 출력
print('-------------------')
print('num_list[2] * 3')
print(num_list[2] * 3)        # (8) list [2]의 값에 3곱한값 출력
print('-------------------')
print('num_list[5 % 4]')
print(num_list[5 % 4])        # (9) list[1] 출력
print('-------------------')
print('len(num_list)')
print(len(num_list))        # (10) list 길이 출력
print('-------------------')
print('min(num_list)')
print(min(num_list))        # (11) list 최솟값 출력
print('-------------------')
print('max(num_list)')
print(max(num_list))        # (12) list 최댓값 출력
print('-------------------')
print('num_list[::3]')
print(num_list[::3])        # (13) 처음부터 3씩 출력
print('-------------------')
print('num_list[1:5]')
print(num_list[1:5])        # (14) 1번인덱스부터 4번인덱스까지 출력
print('-------------------')
print('num_list[-1:-5:-1]')
print(num_list[-1:-5:-1])       # (15) 뒤에서부터 뒤에서 5번째까지 역순으로 출력
print('-------------------')
print('num_list[-5:-1:1]')
print(num_list[-5:-1:1])        # (16) 뒤에서부터 5번째부터 출력
print('-------------------')