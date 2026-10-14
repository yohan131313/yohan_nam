# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 사용자로부터 파일 이름과 삭제할 문자열을 입력받는다. 파일을 열어서 사용자가 원하는 문자열을 삭제한 후에 다시 파일에 쓴다.

filename = input("파일 이름을 입력하시오: ")
target = input("삭제할 문자열을 입력하시오: ")

infile = open(filename, "r", encoding="utf-8")
text = infile.read()
infile.close()

modified_s = text.replace(target, "")

outfile = open(filename, "w", encoding="utf-8")
print(modified_s, file=outfile, end="")
outfile.close()

print("변경된 파일이 저장되었습니다.")