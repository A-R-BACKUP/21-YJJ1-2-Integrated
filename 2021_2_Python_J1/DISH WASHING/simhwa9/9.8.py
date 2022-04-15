# 9.8 다음과 같이 사용자로부터 단어들을 입력받도록 하여라. 입력된 문장은 영문자와 숫자 'Jian777'과 같이 영문자+숫자의 합성으로 이루어진 단어들로 이루어져 있다.
# 이 문장에서 영문자로만 된 단어, 숫자로만 된 단어, 영문자+숫자의 합성으로만 이루어진 단어를 각각 구분하여 나타내어라.
#
# 문장을 입력하시오 : Jian777 is very famous Data scientist. He is only 26 years old but published 19 papers.
# 영문 단어 : is very famous Data scientist He is only years old but published papers
# 숫자 : 26 19
# 영문자+숫자 : Jian777

a = str(input('문장을 입력하시오 : '))          # 문장을 입력 받는다.
b = a.split()           # 문장을 단어 단위로 split 한다.
w = ''          # 영문 단어만을 담을 w 만들기
n = ''          # 숫자만을 담을 n 만들기
wpn = ''            # 영문자+숫자만을 담을 wpn 만들기
for wrd in b:
    if(wrd.isalpha()):          # 영문만 있는 단어라면...
        w += wrd            # w에 추가해주고
        w += ' '            # 띄어쓰기 한번 넣어준다.
    if(wrd.isdigit()):          # 숫자만 있는 단어라면...
        n += wrd            # n에 추가해주고
        n += ' '            # 띄어쓰기 한번 넣어준다.
    if(wrd.isalnum()):          # 영문과 숫자로 이루어진 단어라면...
        if(wrd.isalpha()):          # 영문만 있는 단어는...
            continue            # 거르자
        if(wrd.isdigit()):          # 숫자만 있는 단어는...
            continue            # 거르자
        wpn += wrd          # 그렇게 걸러진 영문자+숫자 단어는 wpn에 추가된다.
        wpn += ' '          # 띄어쓰기 한번 넣어준다.

print('영문 단어 : ', w)            # 영문 단어 출력해주기
print('숫자 : ', n)           # 숫자 단어 출력해주기
print('영문자+숫자 : ', wpn)            # 영문자+숫자 단어 출력해주기