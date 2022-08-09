from turtle import *
color('red', 'yellow')
bgcolor('black')
speed(8)
penup()
left(180)
forward(100)
right(180)
pendown()

begin_fill()
i = 0
while i<36:
    forward(200)
    left(170)
    i+=1
end_fill()
penup()
done()