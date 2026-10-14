# 작성자 202611823 남요한
# 작성일 26.10.14
# 알파벳 a-z사이에 랜덤 10개 출력
import random
import string
random_letters = random.choice(string.ascii_lowercase, k=10)

print("생성된 알파벳 난수 (중복 허용):", "".join(random_letters))