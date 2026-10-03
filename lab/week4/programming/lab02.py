# 작성자 202611823 남요한
# 작성일 26.10.02 
# 문재: 원 클래스 작성
"""원의 넓이와 둘레를 반환하는 getArea()와 getPrimeter()정의"""

import math
class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    def getArea(self):
        return math.pi * self.radius * self.radius
    def getPerimeter(self):
        return 2 * math.pi * self.radius
def main():
    c = Circle(10)
    print("원의 면적", c.getArea())
    print("원의 둘레", c.getPerimeter())
if __name__ == "__main__":
    main()