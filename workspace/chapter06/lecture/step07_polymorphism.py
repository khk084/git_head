# (1) 부모 클래스
class Flight:
    #부모 원형 함수
    def fly(self):
        print('날다, fly 원형 메서드')

# (2) 자식 클래스 : 비행기
class Airplane(Flight):
    #함수 재정의
    def fly(self):
        print('비행기가 날다.')

# (2) 자식 클래스 : 새
class Bird(Flight):
    # 함수 재정의
    def fly(self):
        print('새가 날다.')

# (2) 자식 클래스 : 종이 비행기
class PaperAirplane(Flight):
    # 함수 재정의
    def fly(self):
        print('종이 비행기가 날다.')

# (3) 객체 생성
# 부모 객체 = 자식 객체(자식1, 자식2)
flight = Flight() # 부모 클래스 객체
air = Airplane() # 자식1 클래스 객체
bird = Bird() #자식 2 클래스 객체
paper = PaperAirplane() # 자식 3 클래스 객체

# (4) 다형성
flight.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()