# 작성자 202611823 남요한
# 작성일 26.10.14
# 원을 나타내는 클래스

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented

  
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

   
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    
    def __str__(self):
        return f"Circle(반지름: {self.radius})"

c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(5)


c_sum = c1 + c2
print("c1 + c2:", c_sum)

print("c1 > c2:", c1 > c2)  
print("c1 < c2:", c1 < c2)  
print("c1 == c3 (반지름 비교):", c1.radius == c3.radius)