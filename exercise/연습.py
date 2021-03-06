A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value
class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def minus(self, val):
        self.value -= val
        return self.value

class MaxLimitCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)

print(cal2.value)