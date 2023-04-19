import random

# 변수 정의하기
guesses = 0 # 시도 횟수 기록하기
numMin = 1 # 범위 시작 숫자
numMax = 100 # 범위 끝 숫자
userInput = " " # 사용자 입력 저장하기
# 무작위 숫자 생성하기
randNum = random.randint(numMin, numMax)

# 게임 설명문
print(numMin, "와(과)", numMax, "사이 숫자를 입력해주세요.")

while True :
    guesses += 1
    userInput = int(input("숫자를 입력해주세요."))
    if userInput == randNum :
        print("정답입니다.")
        print("도전 횟수 :", guesses)
        print("즐거우셨나요? 또 만나요!")
        break
    elif userInput > randNum :
        print("그보다 더 작습니다.")
    elif userInput < randNum :
        print("그보다 더 큽니다.")
