# (1) request, BeautifulSoup 모듈 import
import urllib.request #원격 서버 파일 요청
from bs4 import BeautifulSoup # html 파싱

# 요청할 url
url = 'http://www.naver.com/index.html'

# (2) 원격 서버 파일 요청
res = urllib.request.urlopen(url) #웹문서 요청
data = res.read() #text 형태로 읽음

# (3) source 디코딩
src = data.decode("utf-8")
print(src)

# (4) html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# (5) 태그 내용
a = html.find('a')
print('a tag :', a)
print('a tag 내용 :', a.string)