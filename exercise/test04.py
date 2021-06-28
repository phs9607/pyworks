#1번

def is_odd(number):
    if number % 2 == 1 :
        return True
    else:
        return False

num = is_odd(4)
print(num)

#2번

def avg_number(*args):
    result = 0
    for i in args:
        result += i
        print(i, result)
    return result / len(args)

print(avg_number(1, 2))
print(avg_number(1, 2, 3, 4, 5))


#3번

input1 = input("첫번째 숫자를 입력하세요 : ")
input2 = input("두번째 숫자를 입력하세요 : ")

total = int(input1) + int(input2)
print("두수의 합은 %s입니다." % total)

#4번

print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))