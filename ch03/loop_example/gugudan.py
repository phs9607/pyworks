# 구구단 4단 출력하기
dan = int(input("단 입력 : "))
for i in range(1, 10):
    print("%d × %d = %d" % (dan, i , dan*i))
