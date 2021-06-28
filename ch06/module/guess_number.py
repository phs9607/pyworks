import random

com = random.randint(1, 30) #컴퓨터 숫자
while True:
    try:
        guess = int(input("맞혀보세요(1~30) : ")) #사용자 숫
        if guess > 30 or guess < 1:
            print("숫자 범위를 초과하였습니다.")
        elif com < guess:
            print("너무 커요!!")
        elif com > guess:
            print("너무 작아요!!")
        else:
            print("정답!!")
            break
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해 주세요.")

