# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 파일에서 임의의 행을 읽는 Python 프로그램을 작성하시오.[cite: 2]

filename = input("파일 이름을 입력하시오: ")
line_number = int(input("행 번호를 입력하시오: "))

infile = open("/Users/nam-yohan/Documents/Git Hub main/yohan12/lab/week6/input.txt", "r")
lines = infile.readlines()
infile.close()

print(f"{line_number}번 행은 {lines[line_number - 1].strip()}입니다.")

