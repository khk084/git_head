# 1. 변수, 메모리 주소, 자료형
var1 = "Hello python"
print(var1)
print(id(var1))
print(type(var1))
var1 = 100
print(var1)
print(id(var1))
print(type(var1))

var2 = 150.25
print(var2)
print(id(var2))
print(type(var2))

var3 = True
print(var3)
print(id(var3))
print(type(var3))

# 2. 예약어 확인
import keyword # 모듈임포트
python_keyword = keyword.kwlist
print(python_keyword)

print(type(python_keyword))
print(len(python_keyword))

# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

# 정수 -> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

# 논리형 -> 정수
print(int(True))
print(int(False))

# 문자형 -> 정수
st = '10'
print(int(st) ** 2)

# 문장과 단어 추출 예
string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = [] # 문장 저장
words = [] # 단어 저장

# (1) 문단 -> 문장
for sen in string.split(sep = "\n") :
    sents.append(sen)
    # (2) 문장 -> 단어
    for word in sen.split() :
        words.append(word)

print('문장 :', sents)
print('문장 수 :', len(sents))
print('단어 :', words)
print('단어 수 :', len(words))

