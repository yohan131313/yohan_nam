# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: week6/number.txt 파일에 10개의 정수 난수 저장 및 생성 경로 확인

import random
import os

os.makedirs("week6", exist_ok=True)

file_path = "week6/number.txt"
outfile = open(file_path, "w", encoding="utf-8")

for i in range(10):
    n = random.randint(1, 100)
    outfile.write(str(n) + "\n")

outfile.close()

print("파일이 저장된 실제 위치:", os.path.abspath(file_path))