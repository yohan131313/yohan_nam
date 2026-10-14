# 작성자 202611823 남요한
# 작성일 26.10.14
# eval()함수를 사용하여 어떤 문자열을 입력하여도 오류를 일으키지 않고 정수나 실수로 변환하는 코드 작성

user_input = input("정수나 실수를 입력하시오: ")
result = eval(user_input)
print(result)