# 작성자 202611823 남요한
# 작성일 26.10.03
# 문제: 프로그래밍07 PhoneBook클래스

class Person:
    def __init__(self, name, mobile="", office="", email=""):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return f"name: {self.name}\n office phone: {self.office}\n email address: {self.email}"


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile="", office="", email=""):
        self.contacts[name] = Person(name, mobile, office, email)

    def __str__(self):
        res = ""
        for person in self.contacts.values():
            res += str(person) + "\n\n"
        return res.strip()


if __name__ == '__main__':
    pb = PhoneBook()
    pb.add("Kim", office="1234567", email="Kim@company.com")
    pb.add("Park", office="2345678", email="park@company.com")
    print(pb)