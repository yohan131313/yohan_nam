# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍03 박스클래스

class Box:
    def __init__(self, length=1, width=1, height=1):
        self.__length = length
        self.__width = width
        self.__height = height

    def getVolume(self):
        return self.__length * self.__width * self.__height

    def __str__(self):
        return f"({self.__length}, {self.__width}, {self.__height})"


if __name__ == '__main__':
    b1 = Box(100, 100, 100)
    print(b1)
    print(f"상자의 부피는 {b1.getVolume()}")