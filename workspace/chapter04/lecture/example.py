#2 list 원소 추가 및 요소 검사하기
import random
lst = []
vec2 = ' '
vec1 = int(input('vector 수'))

for i in range(vec1) :
     vec2 = random.randint(1,5)
     lst.append(vec2)
     print(vec2)
print('vector 크기:', len(lst))
print(lst)

