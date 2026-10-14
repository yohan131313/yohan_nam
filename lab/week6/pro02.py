# 작성자 202611823 남요한
# 작성일 26.10.13
# 문제: 파일 "input.txt" 안에 저장된 단어 중에서 가장 긴 단어를 찾는 프로그램을 작성하라.

infile = open("/Users/nam-yohan/Documents/Git Hub main/yohan12/lab/week6/input.txt", "r")
text = infile.read()
infile.close()

words = text.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"가장 긴 단어는 {longest_word}입니다.")