# 작성자 202611823 남요한
# 작성일 26.10.14
# 팩토리얼을 계산하는 함수를 작성하기

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
print(f"{n}! = {fact(n)}")