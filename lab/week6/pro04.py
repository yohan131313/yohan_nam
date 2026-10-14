# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 현재 작업 디렉토리에 A.txt, B.txt, ... z.txt 까지 총 26개의 텍스트 파일을 생성하자.

for ch in range(ord('A'), ord('Z') + 1):
    filename = chr(ch) + ".txt"
    outfile = open(filename, "w")
    outfile.write(filename)
    outfile.close()