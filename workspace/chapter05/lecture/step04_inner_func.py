# (1) 일급 함수
def a() : #outer
    print('a 함수')
    def b(): #inner
        print('b 함수')
    return b
b = a()
b()

# (2) 함수 클로저
data = list(range(1, 101))
def outer_func(data):
    dataSet = data # 값(1~100) 생성
    # inner
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg #inner 반환

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

#내부 함수 호출
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg=', avg_val)

# 산포도 구하는 중첩함수 예
from statistics import mean
from math import sqrt

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

# (1) 외부 함수 : 산포도 함수
def scattering_func(data) : #outer
    dataSet = data #data 생성
    # (2) 내부 함수 : 산술평균 반환
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    # (3) 내부 함수 : 분산 반환
    def var_func(avg) :
        diff = [(data - avg) ** 2 for data in dataSet]
        # print(sum(diff)) #차의 합
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val
    # (4) 내부 함수 : 표준편차 반환
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    # 함수 클로저 반환
    return avg_func, var_func, std_func
avg, var, std = scattering_func(data)

# (5) 내부 함수 호출
print('평균 : ', avg())
print('분산 : ', var(avg()))
print('표준편차 :', std(var(avg())))

# (1) 중첩함수 정의
def main_func(num):
    num_val = num # 자료 생성
    def getter() : # 획득자 함수, return 있음
        return num_val
    def setter(value): # 지정자 함수 인수 있음
        nonlocal num_val # nonlocal 명령어
        num_val = value

    return getter, setter # 함수 클로저 반환

# (2) 외부 함수 호출
getter, setter = main_func(100) # 획득한 num 확인

# (3) 획득자 호출
print('num =', getter())

# (4) 지정자 획득
setter(200) #num 값 수정
print('num =', getter()) # num 수정 확인

# (1) 래퍼 함수
def wrap(func) :
    def decorated() :
        print('방가워요!') # 시작부분에 삽입
        func() # 인수로 넘어온 함수 (hello)
        print("잘가요!") # 종료부분에삽입
    return decorated # 클로저 함수 반환

# (2) 함수 장식자 적용
@wrap
def hello() : #이게 func로 넘어간다는데
    print('hi~', "홍길동")

#(3) 함수 호출
hello()


# 재귀함수
# (1) 재귀함수 정의 : 1~n 카운트
def Counter(n):
    if n == 0:
        return 0
    else :
        Counter(n-1)
        print(n, end=' ')

#(2) 함수 호출
print('n=0 :', Counter(0))

#(3) 함수 호출 2
Counter(5)

# (1) 재귀함수 정의 : 1~n 누적합 (1+2+3+4+5=15)
def Adder(n):
    if n == 1 :
        return 1
    else:
        result = n + Adder(n-1)
        print(n, end=' ')
        return result

print('n=1: ', Adder(1))

print('\nn=5 :', Adder(5))