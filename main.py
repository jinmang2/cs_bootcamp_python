from utils import *

# read documentation

# 2학년 3반 담임, User Programmer

raw_data = get_data_from_excel("class_1.xlsx")

scores = raw_data.values()

avrg = get_average(scores)
variance = get_variance(scores, avrg)
std_dev = get_std_dev(variance)

evaluate_class(avrg, variance, std_dev)
