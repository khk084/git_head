from bs4 import BeautifulSoup

# 단계 1. 파일 읽기
file = open("chapter09/data/login.html", mode='r', encoding='utf-8')
source = file.read()

# 단계 2. html 파싱
html = BeautifulSoup(source, 'html.parser')


# 단계 3 태그 찾기
tags = html.find_all('tr')
print(tags)



# 단계 4. 태그 내용 출력
print('th 태그 내용')
for tag in tags:
    th = tag.find('th')
    print(th.string)