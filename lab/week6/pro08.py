# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: scores.txt 파일의 성적을 읽어 파일의 끝에 평균값을 추가하라

infile = open("scores.txt", "r", encoding="utf-8")
scores = []
for line in infile:
    scores.append(float(line.strip()))
infile.close()

average = sum(scores) / len(scores)

outfile = open("scores.txt", "a", encoding="utf-8")
outfile.write(f"평균값: {average}\n")
outfile.close()