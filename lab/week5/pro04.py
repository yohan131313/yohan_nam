# 작성자 202611823 남요한
# 작성일 26.10.13 
# 주사위 게임 프로그램

import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

class FraudDice(Dice):
    def roll(self):
        while True:
            val = super().roll()
            if val > 3:
                return val

dice = Dice()
fraud_dice = FraudDice()

print("일반 주사위 결과:")
for _ in range(5):
    print(dice.roll(), end=" ")
print()

print("가짜 주사위 결과 (3 이하 제외):")
for _ in range(5):
    print(fraud_dice.roll(), end=" ")
print()
