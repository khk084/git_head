# 부모 클래스
class Employee :
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name


# 자식 클래스 - 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print('고용형태:정규직')
        print('이름:', self.name)
        print('급여:', format(self.pay, '3,d'))

# 자식 클래스 - 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('고용형태:임시직')
        print('이름:', self.name)
        print('급여:', format(self.pay, '3,d'))

empType = input("고용형태 선택(정규직<P>, 임시직<T> :")
if empType == 'P' or empType == 'p' :
    p = Permanent(input("이름 :"))
    base = int(input('기본금 :'))
    bonus = int(input('상여금 :'))
    print('=' * 30)
    p.pay_calc(base, bonus)


elif empType == "T" or empType == 't' :
    t = Temporary(input("이름 :"))
    time = int(input('작업시간: :'))
    tpay = int(input('시급 :'))
    print('=' * 30)
    t.pay_calc(tpay, time)

else :
    print('=' * 30)
    print('입력 오류')