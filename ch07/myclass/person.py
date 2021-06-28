# Person 클래스 만들기

class Person:
    def __init__(self): #초기자(생성자 함수)
        self.name = "강하늘"
        self.age = 30

    def getname(self):
        return self.name

    def getage(self):
        return self.age


p = Person() #객체 변수 - 인스턴스
#p.name = "박바다"
#p.age = 30
print(p.getname(), p.getage())

