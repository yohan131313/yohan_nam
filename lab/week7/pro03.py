# 작성자 202611823 남요한
# 작성일 26.10.14
# 람다식을 사용하여 튜플을 정렬하는 프로그램 작성

data = [('국어', 88), ('수학', 90), ('영어', 99), ('자연', 82)]

sorted_data = sorted(data, key=lambda x: x[1])

print(f"원래의 리스트:\n{data}")
print(f"정렬된 리스트:\n{sorted_data}")