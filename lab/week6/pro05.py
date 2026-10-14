# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 왼쪽 파일을 오른쪽 파일로 변환하는 프로그램을 작성하라.

infile = open("/Users/nam-yohan/Documents/Git Hub main/yohan12/lab/week6/learn10.ipynb", "r")
outfile = open("output.txt", "w")

for line in infile:
    outfile.write(line)
    if line.strip() == "line 2":
        outfile.write("line 2-1\n")

infile.close()
outfile.close()