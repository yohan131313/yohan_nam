# 작성자 202611823 남요한
# 작성일 26.10.13 
# 주소를 나타내는 Address와 사람을 나타내는 Person클래스 정의, 연락처를 나타내는 Contact클래스정의
class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

    def get_address(self):
        return f"{self.city} {self.street} (우편번호: {self.zipcode})"


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_person_info(self):
        return f"이름: {self.name} | 전화번호: {self.phone}"


class Contact(Person, Address):
    def __init__(self, name, phone, city, street, zipcode, email=""):
        Person.__init__(self, name, phone)
        Address.__init__(self, city, street, zipcode)
        self.email = email

    def __str__(self):
        return (f"--- [연락처 상세 정보] ---\n"
                f"• {self.get_person_info()}\n"
                f"• 주소: {self.get_address()}\n"
                f"• 이메일: {self.email}")


my_contact = Contact(
    name="홍길동", 
    phone="010-1234-5678", 
    city="청주", 
    street="복대동 대농로", 
    zipcode="28464", 
    email="gildong@example.com"
)

print(my_contact)