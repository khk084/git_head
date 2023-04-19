print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 :'))
h = int(input('사각형의 세로 입력 :'))

class Rectangle:
    width = height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calc(self):
        result = w * h
        return result

    def circum_calc(self):
        result = (w + h) * 2
        return result

obj = Rectangle(w, h)
print('-' * 30)
print('사각형의 넓이 : ', obj.area_calc())
print('사각형의 둘레 : ', obj.circum_calc())
print('-' * 30)
