# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 파일 "input.txt"의 처음 3줄을 읽는 프로그램을 작성하라.

infile = open("/Users/nam-yohan/Documents/Git Hub main/yohan12/lab/week6/input.txt", "r")

for i in range(3):
    line = infile.readline()
    if not line:
        break
    print(line, end="")

infile.close()