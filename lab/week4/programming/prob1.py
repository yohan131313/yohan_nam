# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍01 고양아클래스

class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def __str__(self):
        return f"{self.__name} {self.__age}"


if __name__ == '__main__':
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)

    print(missy)
    print(lucky)
