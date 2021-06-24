#랜덤하게 거북이가 걸러가기

import turtle as t
import random as r

t.shape('turtle')
t.speed(5)
t.bgcolor('pink')
t.setup(500, 500) #작업 영역의 크기

for x in range(100): # 거북이가 100번 움직임
    angle = r.randint(1, 360)
    t.setheading(angle) # 거북이의 방향(각도)
    t.forward(10)
    
