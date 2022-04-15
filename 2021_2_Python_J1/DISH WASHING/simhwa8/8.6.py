# 8.6) 튜플을 요소로 가지는 student_tuple 리스트가 다음과 같이 있다.
# 이 튜플의 요소가 되는 튜플은 (학번, 이름, 전화번호)로 이루어져 있다.

student_tuple = [('211101','강이안','010-123-1111'),
                 ('211102','박동민','010-123-2222'),
                 ('211103','김수정','010-123-3333')]
student={}
print('첫번째 문제')
for i in range(len(student_tuple)):         # 튜플의 길이만큼 반복
    student[student_tuple[i][0]]=student_tuple[i][1]    # student 딕셔너리에 튜플 대입
for key,value in student.items():
    print(key,':',value)            # 모두 출력하기

student={}
for i in range(len(student_tuple)):     # 길이만큼 반복
    student[student_tuple[i][0]]=student_tuple[i][1],student_tuple[i][2]
    # student 딕셔너리에 튜플 대입
print('두번째 문제')
x = input('학번을 입력하세요 : ')
print('{} 학생은 {}이며, 전화번호는 {}입니다.'.format       # 딕셔너리에 키와 밸류 값 출력
      (x, student[x][0],  
              student[x][1]))