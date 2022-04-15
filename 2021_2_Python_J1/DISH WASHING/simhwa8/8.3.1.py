# 8.3.1) 이 튜플을 수정하여 { 학번 : [이름, 전화번호] }의 쌍으로 이루어진 딕셔너리를 만들어서 출력하여라

student_tup = (('211101','최성훈','010-1234-4500'),
       ('211102','김은지','010-2230-6540'),
       ('211103','이세은','010-3232-7788'))
student = {}      # 딕셔너리 초기화
for i in range(len(student_tup)):        # 튜플의 길이만큼 반복한다.
    student[student_tup[i][0]]=[student_tup[i][1],student_tup[i][2]]
    # 학생 정보 넣기
for key,value in student.items():       # 키값과 밸류값 출력하기 위해 반복
    print('{',key,value,'}')        # 출력한다