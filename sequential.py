import openpyxl
import math
from functools import reduce
#학년 전체 학생의 평균 : 50점

#파일에서 데이터 읽기
raw_data = {}
wb = openpyxl.load_workbook('class_1.xlsx')
ws = wb.active
g = ws.rows

for name, score in g:
    raw_data[name.value] = score.value

#print("raw_data : ", raw_data)

#학생들 점수
scores = list(raw_data.values())

#평균 구하기
avrg = reduce(
            lambda a, b:
            a + b,
            scores)/len(scores)

#분산 구하기
variance = round(
    reduce(
        lambda a, b:
        a + b,
        map(
            lambda s:
            (s-avrg)**2,
            scores))/len(scores),
    1)

#표준 편차 구하기
std_dev = round(
    math.sqrt(variance),
    1)


#출력 부분

print(
    "평균 :{0}, 분산 : {1}, 표준 편차 : {2}".format(
    avrg, variance, std_dev))

if avrg <50 and std_dev >20:
    print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
elif avrg > 50 and std_dev >20:
    print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and std_dev <20:
    print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and std_dev <20:
    print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
