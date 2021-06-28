import time

print(time.time()) # 1970년 1

print(time.localtime())

print(time.ctime()) # 날짜와 시간 요일 표시

print(time.strftime('%x', time.localtime()))

print(time.strftime('%x', time.localtime(time.time())))

#time.sleep(1) : 1초간 대기
#파이썬에서는 1초를 1로 표
for i in range(1, 11):
    print(i)
    time.sleep(i)
