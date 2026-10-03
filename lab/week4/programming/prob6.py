# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍06 Person클래스

class Person:
    def __init__(self, name, mobile="", office="", email=""):
        self.__name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def __str__(self):
        return f"name: {self.__name}\n office phone: {self.office}\n email address: {self.email}"


if __name__ == '__main__':
    p1 = Person("Kim", office="1234567", email="Kim@company.com")
    p2 = Person("Park", office="2345678")
    p2.setEmail("park@company.com")

    print(p1)
    print(p2)