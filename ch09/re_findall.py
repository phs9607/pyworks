import re
str = "Too is too"
f1 = re.findall("T[ow]o", str) #대소문자구분
print(f1)

f2 = re.findall("T[ow]o", str, re.IGNORECASE) #대소문자 구분하지않음
print(f2)

f3 = re.findall("t[^w]o", str, re.IGNORECASE)
print(f3)