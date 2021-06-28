class Students:
    def __init__(self, sid, name):
        self.__sid = sid
        self.__name = name

    def getsid(self):
        return self.__sid

    def getname(self):
        return self.__name

s1 = Students(1001, "김산")
print(s1.getsid(), s1.getname())
s2 = Students(1002, "이강")
print(s2.getsid(), s2.getname())