# 작성자 202611823 남요한
# 작성일 26.10.14
# 이터레이터를 구현하는 클래스 작성

class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        result = (self.index, self.data[self.index])
        self.index += 1
        return result

for index, letter in MyEnumerate('abc'):
    print(f"{index} : {letter}")