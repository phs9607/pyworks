#정규 표현식 예제
import re

#p = re.compile('a.b') #+는 반복을 의미하는 메타문자
p = re.compile('a+b')
m = p.match('aaaab')
print(m)
print(m.group())

