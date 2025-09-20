from turtle import *

def draw_bear():
    speed(5)
    pensize(5)
    bgcolor("white")


    #head
    penup()
    goto(0, -150)
    pendown()
    fillcolor("gold")
    begin_fill()
    circle(150)
    end_fill()

    #eyes
    penup()
    goto(-45, 55)
    pendown()
    fillcolor("black")
    begin_fill()
    seth(90)
    for i in range(2):
        circle(15, 90)  
        circle(7, 90)  
    end_fill()

    penup()
    goto(60, 55)
    pendown()
    fillcolor("black")
    begin_fill()
    seth(90) 
    for i in range(2):
        circle(15, 90)  
        circle(7, 90)  
    end_fill()

    #nose
    penup()
    goto(15, -10)
    pendown()
    fillcolor("black")
    begin_fill()
    circle(15)
    end_fill()

    #mouse
    penup()
    goto(-45, -40)
    seth(-60)
    pendown()
    circle(50, 120) 

    done()

# 测试
draw_bear()
