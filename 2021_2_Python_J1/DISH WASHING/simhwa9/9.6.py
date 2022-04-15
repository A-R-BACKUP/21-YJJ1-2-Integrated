# 9.6 다음과 같은 문장이 있다. 이 문장에서는 'English = 98'와 같이 과목과 점수가 저장되어 있다.
# 이 문장을 분석하여 숫자로 이루어진 점수를 읽어서 합과 평균점수를 출력하여라.
#
# 문장 s : English = 89, Science = 90, Math = 92, History = 80.
# 총점 : 351
# 평균점수 : 87.75

s = 'English = 89, Science = 90, Math = 92, History = 80.'          # s에 문장 주입
eng = s[10:12]          # 영어 점수 추출
sci = s[24:26]          # 과학 점수 추출
mat = s[35:37]          # 수학 점수 추출
his = s[49:51]          # 역사 점수 추출
all = int(eng) + int(sci) + int(mat) + int(his)         # 각 점수를 문자형에서 정수형으로 변환 후 모두 합하기
avg = all / 4           # 평균점수 계산

print('문장 s : English = 89, Science = 90, Math = 92, History = 80.')
print('총점 : ', all)         # 총점 출력하기
print('평균점수 : ', avg)           # 평균점수 출력하기