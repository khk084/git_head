import os # os 모듈 import

#현재 작업 디렉터리 경로 확인
os.getcwd()


# 작업 디렉터리 변경
os.chdir('chapter08')
os.getcwd()

# 현재 작업 디렉터리 목록
os.listdir('.')

# 디렉터리 생성 : 'test' 생성
os.mkdir('test')
os.listdir('.')

# 디렉터리 이동 : 'test' 이동
os.chdir('test')
os.getcwd()
print(os.getcwd())

# 여러 디렉터리 생성 : 'test2', 'test3' 생성
os.makedirs('test2/test3')
os.listdir('.')

# 디렉터리 이동
os.chdir('test2')
os.listdir('.')

#디렉터리 삭제
os.rmdir('test3')
os.listdir('.')

# 상위 디렉터리 이동 : 상위 디렉터리 2개 이동
os.chdir('../..')
os.getcwd()
print(os.getcwd())

# 여러개의 디렉터리 삭제
os.removedirs('test/test2')
os.chdir('..')
import os.path
# 현재 경로 확인
os.getcwd()
print(os.getcwd())

#경로 변경
os.chdir('chapter08')
print(os.getcwd())

# lecture 디렉터리의 step01_try_except.py 파일 절대경로
os.path.abspath('lecture/step01_try_except.py')

# step01_try_except.py 파일의 디렉터리 이름
os.path.dirname('lecture/step01_try_except.py')

# workspace 디렉터리 유무 확인
os.path.exists('D:\\git_office\\workspace')

# step01_try_except.py 파일 유무 확인
os.path.isfile('lecture/step01_try_except.py')

# 디렉터리와 파일 분리
os.path.split("c:\\test\\test1.txt")
# 디렉터리와 파일 결합
os.path.join('c:\\test', 'test1.txt')

# step01_try_except.py 파일크기
os.path.getsize('lecture/step01_try_except.py')