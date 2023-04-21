# (1-1) json 인코딩
import json
user = { 'id':1234, 'name':'홍길동'}
print(type(user))
print(user['name'])

# (1-2) json 인코딩
JsonString = json.dumps(user, ensure_ascii=False) #ASCII 인코딩 방식 적용 안함

# 문자열 출력
print(JsonString)
print(type(JsonString))


# (2) json 디코딩
pyObj = json.loads(JsonString)
print(type(pyObj))

# Dict 자료 확인
print(pyObj['name'])
for key in pyObj:
    print(key, ':', pyObj)


# (1) json file 읽기
file = open('chapter08/data/usagov_bitly.txt', mode='r', encoding='utf-8')
lines = file.readlines()

# (2) json 디코딩
#file (json 문자연) -> python dict 객체
rows = [json.loads(row) for row in lines]
print('rows :', len(rows))

# (3) 10개 원소 출력
for row in rows[:10]:
    print(row)
    print(type(row))
file.close()

# (4) dict -> DataFrame 변환
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())