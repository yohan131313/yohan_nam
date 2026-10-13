# 작성자 202611823 남요한
# 작성일 26.10.13 
# 2차원공간의 한점을 나타내는 클래스를 정의하고 3차원공간의 클래스 정의
class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)
        
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

p = Point3D(10, 20, 30)
print(p)