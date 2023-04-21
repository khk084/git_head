from bs4 import  BeautifulSoup #html 파싱

# (1) 로컬 파일 읽기
file = open('chapter09/data/html02.html', mode='r', encoding='utf-8')
source = file.read()

# (2) html 파싱
html = BeautifulSoup(source, 'html.parser')

# (3) a 태그 찾기
links = html.find_all('a') #list 반환
print('links size=', len(links))

# (4) a 태그에서 속성 찾기
for link in links:
    try:
        print(link.attrs['href']) #5개
        print(link.attrs['target']) #error(1,2,4,5)

    except Exception as e:
        print('예외 발생 : ', e)


# (5) 정규 표현식으로 속성 찾기
import re
print('패턴 객체 이용 속성 찾기')
patt=re.compile('http://') #pattern object 생성
links = html.find_all(href = patt)
print(links)