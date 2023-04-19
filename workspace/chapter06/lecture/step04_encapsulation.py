class Account:
    # (1) 은닉 멤버변수
    __balance = 0
    __accName = None
    __accNo = None

    # (2) 생성자 : 멤버변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    # (3) 계좌정보 확인 : Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # (4) 입금하기 : Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return # 종료
        self.__balance += money

    # (5) 출금하기 : Setter
    def withdraw(self, money):
        if self.__balance < money :
            print('잔액 부족')
            return
        self.__balance -= money

# (6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41')

# (7) Getter 호출
bal = acc.getBalance()
print('계좌정보 :', bal)

# (8) Setter 호출
acc.deposit(10000)
bal = acc.getBalance()
print('계좌정보 :', bal)