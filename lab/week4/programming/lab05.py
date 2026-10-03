# 작성자 202611823 남요한
# 작성일 26.10.03
# 문재: 백터 객체에 특수 메소드 정의하기

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)


v1 = Vector2D(0, 1)
v2 = Vector2D(1, 0)
v3 = Vector2D(1, 1)

a = v1 + v2

print(a)
print(v1 == v2)
print(a == v3)
print(v1 - v2)