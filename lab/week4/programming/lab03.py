# 작성자 202611823 남요한
# 작성일 26.10.02 
# 문재: 자동차 클래스 작성
"""자동차를 나타내는 Car클래스를 작성하고 이 클래스로 부터 몇가지 객체를 생성"""


class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

myCar = Car(0, "빨강", "소나타")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)

myCar.drive()

print("자동차의 속도는", myCar.speed)

    