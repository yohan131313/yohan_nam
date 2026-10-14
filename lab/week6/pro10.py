# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 텍스트 파일을 열어서 파일 안의 스페이스 문자의 개수와 탭의 개수를 세는 프로그램을 작성하여 보자.

filename = input("파일 이름을 입력하시오: ")

infile = open(filename, "r", encoding="utf-8")
text = infile.read()
infile.close()

space_count = text.count(" ")
tab_count = text.count("\t")

print(f"스페이스 수 = {space_count}, 탭의 수 = {tab_count}")
