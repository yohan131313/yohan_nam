# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 은행계좌
""" 이 프로그램은 은행 계좌를 클래스로 정의 """

class BacnkAccont:
    def __init__(self):
        self.__balance = 0
    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에",amount,"가 입금되었음")
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        print("통장에서", amount, " 가 출금되었음")
        return self.__balance

a = BacnkAccont()
a.deposit(100)
a.withdraw(10)