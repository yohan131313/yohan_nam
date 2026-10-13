
# 작성자 202611823 남요한
# 작성일 26.10.13 
# 일반적인 함수를 나타내는 Function클래스를 정의하고 2차방정식을 나타내는 클래스 Quardratic을 정의

import cmath

class Function:
    def __init__(self):
        pass

    def value(self, x):
        raise NotImplementedError("값이 아직 결정되지 않았습니다.")

class Quadratic(Function):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

    def get_roots(self):
        d = cmath.sqrt(self.b ** 2 - 4 * self.a * self.c)
        root1 = (-self.b + d) / (2 * self.a)
        root2 = (-self.b - d) / (2 * self.a)
        return (root1, root2)

q = Quadratic(1, -3, 2)
print("방정식의 근:", q.get_roots())