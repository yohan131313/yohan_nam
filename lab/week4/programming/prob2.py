# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍02 로켓클래스

class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y += 1

    def __str__(self):
        return f"로켓의 높이: {self.y}"


if __name__ == '__main__':
    myRocket = Rocket()
    print(myRocket)
    myRocket.moveUp()
    print(myRocket)