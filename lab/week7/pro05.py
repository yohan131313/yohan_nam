# 작성자 202611823 남요한
# 작성일 26.10.14
# 람다식을 사용하여 주어진 정수 리스트에사 모든 숫자를 세제곱하는 프로그램
number = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x : x**3 , number ))
print(result)