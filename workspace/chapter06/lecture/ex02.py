from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

# 산포도 클래스
class Scattering:
    # 생성자

    def __init__(self):
       pass

    def data(self, x):
        self.x = x

    # 메서드 : 분산(var_func)
    def var_func(self):
        avg = mean(x)
        diff = [(X - avg) ** 2 for X in x]
        result = sum(diff) / (len(x) - 1)
        print('분산:', result)

    # 메서드 : 표준편차(std_func)
    def std_func(self):
        avg = mean(x)
        diff = [(X - avg) ** 2 for X in x]
        result = sqrt(sum(diff) / (len(x) - 1))
        print('표준편차:', result)

obj = Scattering()
obj.data(x)
obj.var_func()
obj.std_func()
