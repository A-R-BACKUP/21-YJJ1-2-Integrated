# 8.5) LAB 8-2번 문제를 확장하여라. 확장할 명령은 v로 이를 입력할 경우 다음과 같이 사전에 등록된 단어와 그 뜻을 출력한다

print('사전 프로그램 시작... 종료는 q를 입력')
dictionary = {}     # 튜플 초기화

while True:         # 무한 반복문
    st = input('$')     # 찾는문
    command = st[0]     #st[0]번째문자를 command에 대입
    if command == '<':      #만약 command가 < 라면
        st = st[1:]     # st는 1번쨰문자빼고 나머지를 대입
        inputStr = st.split(':')        # ':'을 기준으로 문자열 나눔
        if len(inputStr) < 2:       # 만약 문자열이 2개 이상이라면
            print('입력 오류가 발생했습니다.')     # 오류 출력하기
        else:
            dictionary[inputStr[0].strip()]= inputStr[1].strip()
            # 아닐시에 튜플에 대입
    elif command == '>':        # 만약 command가 > 라면
        st = st[1:]     # st는 1번쨰문자빼고 나머지를 대입
        inputStr = st.strip()       # inputStr에 공백제외한 문자열 대입
        if inputStr in dictionary:      # 만약 문자열과 딕셔너리의 키가 같다면
            print(dictionary[inputStr])     # 딕셔너리에 해당하는 밸류 출력
        else:
            print('{}가 사전에 없습니다'.format(inputStr))  # 없을 시 출력
    elif command == 'q':    # q 입력시
        break               # 종료하기
    elif command == 'v':        # v 입력시
            print('영어 사전에 있는 단어와 뜻을 출력합니다.' ) # 출력하기
            for key,value in dictionary.items():
                # .items함수를 사용해 딕셔너리 키와 밸류 값 다 출력
                print(key,': ',value)               # 출력하기
    else:
        print('입력 오류가 발생했습니다')       # 오류 출력하기
print('사전 프로그램을 종료합니다')         # 종료시 종료 안내 출력 후 종료