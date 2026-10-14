# 작성자 202611823 남요한
# 작성일 26.10.14
# map과filter을 사용하여 짝수값의 제곱으로 새로운 리스크를 만드는 프로그램

number = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x%2==0,number)
result2 = map(lambda x : x**2 , result )
print(list(result2))