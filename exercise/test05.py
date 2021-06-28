# 1번

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value
c = Calculator()
print(c.add(10))
print(c.value)


cal = UpgradeCalculator()
print(c.add(10))
cal.minus(7)
print(cal.value)

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)
