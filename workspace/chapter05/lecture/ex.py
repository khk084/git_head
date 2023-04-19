def StarCount(height):
    if height == 0 :
        return 0
    else:
        result = height + StarCount(height-1)

        print('*' * height)
        return result

height = int(input('height :'))

print('start 개수: %d' %StarCount(height))

# 문제 2
def bank_account(bal):
    balance = bal # 잔액 초기화

    def getBalance():
        return balance

    def deposit(money):
        nonlocal balance
        balance += money
    def withdraw(money):
        nonlocal balance
        balance -= money
    return getBalance, deposit, withdraw

bal = int(input('최초 계좌의 잔액을 입력하세요'))
getBalance, deposit, withdraw = bank_account(bal)
print('현재 계좌 잔액은 %d원 입니다.' %getBalance())
money = int(input("입금액을 입력하세요."))
deposit(money)
print('%d원 입금 후 잔액은 %d원입니다.' %(money, getBalance()))
money = int(input("출금액을 입력하세요."))
withdraw(money)
if getBalance() < money:
    print('잔액이 부족합니다.')
else:
    print('%d원 출금 후 잔액은 %d원입니다.' % (money, getBalance()))



