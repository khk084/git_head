email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

from re import findall, match
for e in email.split(sep='\n'):
    print((findall('^[a-z]{,1}[a-z0-9]{3,}@[a-z]{3,}.[a-z]{,3}', e)))
