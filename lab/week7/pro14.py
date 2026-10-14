# 작성자 202611823 남요한
# 작성일 26.10.14 
# 100과 200 사이에 5개의 짝수난수 출력

import random

random_numbers = [random.choice(range(100, 201, 2)) for _ in range(5)]

print("생성된 난수:", random_numbers)