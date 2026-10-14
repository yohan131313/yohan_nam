# 작성자 202611823 남요한
# 작성일 26.10.14
# map을 사용하여 요소를 제곱하는 프로그램

number = [1,2,3,4,5,6,7,8,9,10]
result = map(lambda x : x**2 , number )
print(list(result))