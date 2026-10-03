# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍05 triangle클래스

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def checkAngles(self):
        return (self.angle1 + self.angle2 + self.angle3) == 180


if __name__ == '__main__':
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())