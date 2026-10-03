# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 프로그래밍04 Rectangle클래스

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        no_overlap = (self.x + self.width <= r.x or
                      r.x + r.width <= self.x or
                      self.y + self.height <= r.y or
                      r.y + r.height <= self.y)
        return not no_overlap


if __name__ == '__main__':
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")