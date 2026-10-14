# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 텍스트 파일에서 특정 단어를 찾아 다른 단어로 변경하는 프로그램을 작성하시오.

filename = input("파일 이름을 입력하시오: ")
old_word = input("변경할 단어를 입력하시오: ")
new_word = input("새로운 단어를 입력하시오: ")

infile = open(filename, "r", encoding="utf-8")
text = infile.read()
infile.close()

modified_text = text.replace(old_word, new_word)

outfile = open(filename, "w", encoding="utf-8")
outfile.write(modified_text)
outfile.close()

print("파일의 단어가 성공적으로 변경되었습니다.")