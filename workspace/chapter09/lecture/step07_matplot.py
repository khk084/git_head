# (1) 패키지 import
import matplotlib.pyplot as plt
import random

# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# (2) 차트 자료 생성
print(random.randint(a=1, b=5))
print(random.random())
print(random.normalvariate(mu=0, sigma=1))

# (1) plot() 함수 도움말
# help(plt.plot)

# (2) 기본 차트 그리기

# (2-1) 1개 data
data = range(10) # range(n) 동일 0-9
plt.plot(data)
plt.plot(data, 'r+')

# (2-2) 2개 data
data2 = [random.random() for i in range(10)]
plt.plot(data2)
plt.plot(data, data2, 'ro')


# (1) 산점도 그리기

# (1-1) 단색 산점도
plt.scatter(x=data, y=data2, c='b', marker='o')

# (1-2) 여러가지 색 산점도
cdata = [random.randint(a=1, b=3) for i in range(10)]
plt.scatter(x=data, y=data2, c=cdata, marker='o')

# (2) 히스토그램
data3 = [random.normalvariate(mu=0, sigma=1) for i in range(1000)]
plt.hist(data3) # 정규 분포

data4 = [random.uniform(a=1, b=100) for i in range(1000)]
plt.hist(data4) #균등 분포