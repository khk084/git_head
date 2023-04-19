# re 모듈관련 함수 import
from re import findall, sub

# 텍스트 전처리
texts = ['우리나라  대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

# (1) 텍스트 전처리 함수
def clean_text(text) : # 문장 인수
    # 1~6단계
    texts_re = text.lower()
    texts_re2 = sub("[0-9]", '', texts_re)
    texts_re3 = sub('[,.?!:;]', '', texts_re2)
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3)
    texts_re5 = sub('[a-z]', '', texts_re4)
    texts_re6 = ' '.join(texts_re5.split())
    return texts_re6

# (2) 함수 호출
texts_result = [clean_text(text) for text in texts]
print(texts_result)
