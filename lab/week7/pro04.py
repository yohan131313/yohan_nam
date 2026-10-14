# 작성자 202611823 남요한
# 작성일 26.10.14
# 람다식을 사용하여 정수 리스트를 필터링 하는 프로그램
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result1 = list(filter(lambda x: x % 2 == 1, number))
result2 = list(filter(lambda x: x % 2 == 0, number))

print("홀수:", result1)
print("짝수:", result2)