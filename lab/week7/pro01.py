# 작성자 202611823 남요한
# 작성일 26.10.14
# 3의배수 갯수를 세는 프로그램

count = len([x for x in range(1, 101) if x % 3 == 0])

print(f"3의 배수의 개수 = {count}")