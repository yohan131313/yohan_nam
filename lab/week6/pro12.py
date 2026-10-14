# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 텍스트 파일을 읽어 파일의 행 수, 단어 수, 문자 수를 세는 프로그램을 작성하라.

filename = input("파일 이름을 입력하시오: ")

infile = open(filename, "r", encoding="utf-8")
text = infile.read()
infile.close()

lines = text.splitlines()
words = text.split()
chars = len(text)

print(f"행 수: {len(lines)}")
print(f"단어 수: {len(words)}")
print(f"문자 수: {chars}")