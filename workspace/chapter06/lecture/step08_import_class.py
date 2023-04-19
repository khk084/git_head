# (1) 리스트 열거형 객체 이용
lst = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인: ', i, end=', ')
    print('내용 :', c)

# (2) 튜플 열거형 객체 이용
dit = {'name' : '홍길동', 'job': '회사원', 'addr':'서울시'}
for i, k in enumerate(dit) :
    print('순서: ', i, end=', ')
    print('키:', k, end=', ')
    print('값: ', dit[k])


# (1) 모듈 내장 클래스 import
import datetime #모듈 import
from datetime import date, time

# (2) date 클래스
help(date)

today = date(2019, 10, 23) # date 객체 생성
print(today) # date 객체 정보

# date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)

# date 객체 메서드 호출
w = today.weekday()
print('요일 정보 : ', w)

# (3) time 클래스
help(time)

currTime = time(21, 4, 30) # time 객체 생성
print(currTime) # time 객체 정보

# time 객체 멤버변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

# time 객체 메서드 호출
isoTime = currTime.isoformat()
print(isoTime)

