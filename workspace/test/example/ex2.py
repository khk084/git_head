# 1
weight = input('짐의 무게는 얼마입니까?')
while int(weight) < 10 :
    print('수수료는 없습니다.')
    break
else :
    s = int(weight) // 10
    print('수수료는 %d원 입니다.' %(int(s) * 10000))

while True :
    weight = int(input('짐의 무게는 얼마입니까?'))
    if weight == 0 :
        break;
    if weight >= 10 :
        price = (weight // 10) * 10000
        print('수수료는 ' + format(price, '3,d') + '입니다')
    else :
        print('수수료는 없습니다.')

# 2
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

#sents = []

for word in multiline.split() :
    print(word)

#for sen in multiline.split('\n') :
#    sents.append(sen)
#    for word in sen.split() :
#        print(word)

cnt = 0
doc = []
word = []
for line in multiline.split("\n") :
    doc.append(line)
    for w in line.split():
        word.append(w)
        print(w)
        cnt += 1
print('단어수 :', cnt)
print(doc)
print(word)
