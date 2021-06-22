# 1번 문제
kor = 80
eng = 75
math = 55
sum = kor + eng + math
avg = sum / 3
print("평균 : ",  avg)

# 2번 문제
print(13 % 2)
n = 13
if n % 2 == 0:
    print("짝수")
else:
    print("홀")
 
# 3번 문제
pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[7:]

print(yyyymmdd)
print(num)

# 4번 문제
gender = pin[7]
if gender == "1":
    print("남자입니다.")
else:
    print("여자입니다.")

# 5번 문제
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6번 문제
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 7번 문제
a = ['Lite', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# split() 예제
msg = "Lite is too short"
msg = msg.split() # 구분기호 공백
print(msg)

s = "a:b:c:d"
s = s.split(':')
print(s)
