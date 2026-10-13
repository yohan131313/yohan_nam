# 작성자 202611823 남요한
# 작성일 26.10.13 
# 대학교에서 학과,교과목,학생을 등록하는 프로그램
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, name, credits):
        course = Course(name, credits)
        self.courses.append(course)
        return course

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.students = []

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)

dept = Department("컴퓨터")
math1 = dept.add_course("공업수학", 3)
math2 = dept.add_course("이산수학", 2)

kim = Student("김", 20200001)
kim.enroll(math1)

print(f"학과: {dept.name}")
print(f"개설된 교과목: {[c.name for c in dept.courses]}")
print(f"학생 이름: {kim.name}, 학번: {kim.student_id}")
print(f"신청한 과목: {[c.name for c in kim.courses]}")
print(f"공업수학 수강생: {[s.name for s in math1.students]}")