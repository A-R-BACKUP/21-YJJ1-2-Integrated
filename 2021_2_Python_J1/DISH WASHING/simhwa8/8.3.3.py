# 8.3.3) student_tup의 마지막 항목으로 직전학기의 학점을 추가하여라.
# 세 학생의 학점은 각각 4.3, 3.9, 4.25이다.
# 이 정보를 바탕으로 다음과 같은 딕셔너리를 만들어서 학생 정보를 출력하여라

student_tup = (('211101','최성훈','010-1234-4500',4.3),
               ('211102','김은지','010-2230-6540',3.9),
               ('211103','이세은','010-3232-7788',4.25))
student = {}      # 딕셔너리 초기화
for i in range(len(student_tup)):       # 튜플의 길이만큼 반복한다.
    student[student_tup[i][0]]=student_tup[i][1],[student_tup[i][2],student_tup[i][3]]
    # 학생 정보와 성적 대입
for key,value in student.items():   #키값 밸류값 출력
    print('{',key,value,'}')    #출력