# 작성자 202611823 남요한
# 작성일 26.10.14
# 호출 될 대마다 앞의 수에 1을 더하여 반환하는 함수 제너레이터를 이용해 구현

def counter_generator():
    count = 0
    while True:
        count += 1
        yield count

counter = counter_generator()

print(next(counter))  
print(next(counter))  
print(next(counter))  
print(next(counter))  