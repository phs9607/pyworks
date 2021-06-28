# Person 클래스 - 멤버 변수(name, age)
#Employee 클래스는 Person을 상속받음
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    pass

if __name__ == "__main__":
    p = Person("한강", 25)
    print(p.name, p.age)

    e1 = Employee("남한강", 30)
    print(e1.name, e1.age)

    e2 = Employee("북한강", 35)
    print(e2.name, e2.age)