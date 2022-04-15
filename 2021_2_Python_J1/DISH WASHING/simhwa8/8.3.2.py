# 8.3.2) 이 정보를 이용하여 학생의 학번을 입력으로 받아서 이름과 전화번호를 출력하는
# 학사 정보 프로그램을 작성하여라.

student_tup = (('211101','최성훈','010-1234-4500'),
               ('211102','김은지','010-2230-6540'),
               ('211103','이세은','010-3232-7788'))
student = {}      # 딕셔너리 초기화

for i in range(len(student_tup)):        # 튜플의 길이만큼 반복한다.
    student[student_tup[i][0]]=[student_tup[i][1],student_tup[i][2]]
    # 학생 정보 넣기

h = input('학번을 입력하시오 : ')       # 학번 입력 받기
if h in student:        # h를 studnet에 대입
    print('이름 :',student[h][0])     # 입력 된 값인 h에 맞는 값 출력
    print('연락처',student[h][1])      # 입력 된 값인 h에 맞는 값 출력
else:
    print('다시 입력하시오')       # 입력한 학번이 튜플에 있지 않은 경우 출력