# 작성자 202611823 남요한
# 작성일 26.10.13 
# Animal 클래스와 고양이 객체
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

def get_oldest_cat(*args):
    return max(args, key=lambda cat: cat.age)

cat1 = Cat("나비", 3, "코숏")
cat2 = Cat("야옹이", 7, "페르시안")
cat3 = Cat("루비", 5, "러시안블루")

oldest = get_oldest_cat(cat1, cat2, cat3)
print(f"가장 나이가 많은 고양이는 {oldest.age}살입니다.")