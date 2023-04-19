# (1) 현재 작업디렉터리
import os
print('\n현재 경로:', os.getcwd())

# (2) 예외처리
try:
    # (3) 파일 읽기
    ftest1 = open('chapter08/data/ftest.txt', mode = 'r')
    print(ftest1.read()) # 전체 파일 읽기

    # (4) 파일 쓰기
    ftest2 = open('chapter08/data/ftest2.txt', mode = 'w')
    ftest2.write('my first text~~~') # 파일 쓰기

    # (5) 파일 쓰기 + 내용 추가
    ftest3 = open('chapter08/data/ftest2.txt', mode='a')
    ftest3.write('\nmy second text~~~') # 파일 쓰기(추가)

except Exception as e:
    print('Error 발생:', e)

finally:
    ftest1.close() # 파일 객체 닫기
    ftest2.close()
    ftest3.close()



# 파일 읽기 관련 함수
try :

    # (1) read() : 전체 텍스트 자료 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    # (2) readlines() : 전체 텍스트 줄 단위 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    lines = ftest.readlines() # list 반환
    print(lines)
    print(type(lines)) # <class 'list'>
    print('문단 수:', len(lines))

    # (3) list -> 문장 추출
    docs = [] # 문장 저장
    for line in lines:
        print(line.strip())
        docs.append(line.strip())

    print(docs)

    # (4) readline() : 한 줄 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    line = ftest.readline() # 한 줄 읽기
    print(line)
    print(type(line))

except Exception as e:
    print('Error 발생: ', e)

finally:
    #파일 객체 닫기
    ftest.close()

try:
    with open('chapter08/data/ftest3.txt', mode='w', encoding='utf-8') as ftest:
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2')
        # with 블록 벗어나면 자동 close

    with open('chapter08/data/ftest3.txt', mode='r', encoding='utf-8') as ftest:
        print(ftest.read())

except Exception as e:
    print('Error 발생 :', e)
finally:
    pass