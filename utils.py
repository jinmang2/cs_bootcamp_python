from openpyxl import load_workbook
import math
from functools import reduce

# 절차지향
# - 함수 이름만 봐도 어떤 기능을 하는지 알아야 한다.
# - 어떤 인자를 받을 것이고 반환값은 무엇으로 할 것인지

def get_data_from_excel(filename):
    raw_data = {}
    wb = load_workbook(filename)
    ws = wb.active
    g = ws.rows
    
    for name, score in g:
        raw_data[name.value] = score.value
        
    return raw_data

def get_average(scores):
    
    """
    get_average(scoes)->real number
    scores : the list of student's score
    returns : 평균
    """
    
    return reduce(
            lambda a, b:
            a + b,
            scores)/len(scores)

def get_variance(scores, avrg):
    return round(
    reduce(
        lambda a, b:
        a + b,
        map(
            lambda s:
            (s-avrg)**2,
            scores))/len(scores),1)

def get_std_dev(variance):
    return round(
        math.sqrt(variance),1)

def evaluate_class(avrg, variance, std):
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
        
# porting 완료
