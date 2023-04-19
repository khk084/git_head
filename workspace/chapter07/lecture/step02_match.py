from re import match
# (1) 패턴과 일치된 경우
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)

if result :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')

# (2) 패턴과 불일치된 경우
jumin = '123456-5234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)

if result :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')