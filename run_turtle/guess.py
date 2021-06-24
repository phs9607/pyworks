import random

com = random.randint(1, 30) #컴퓨터 숫자
while True:
    guess = int(input("맞혀보세요(1~30) : ")) #사용자 숫
    if com < guess:
        print("너무 커요!!")
    elif com > guess:
        print("너무 작아요!!")
    else:
        print("정답!!")
        break

