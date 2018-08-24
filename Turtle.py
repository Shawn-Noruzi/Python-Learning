#Author: Shayan Noruzi 301179543
#Date Revised: 2015/03/02
#Hours spent on assignment:4
#Turtle program

import turtle as t
import random


def randomcolor():
    t.colormode(255)
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    randcol=(red,green,blue)
    return randcol


    return
def spiral():
    for i in range(25):
        for i in range(1,7):
            t.pencolor(randomcolor())
        t.forward(75)
        t.right(123)
    return

def hexagonRight():
    for i in range (1,7):
        for i in range(1,7):
            t.pencolor(randomcolor())
        t.forward(50)
        t.right(60)
    return

def coolpattern():
    for i in range(12):
        hexagonRight()
        t.right(30)
    return

def shape(side,degree):
    t.fillcolor(randomcolor())
    t.begin_fill()
    for i in range(10):
        t.forward(side)
        t.right(45)
        t.pencolor("black")
        for i in range(2):
            t.pencolor("pink")
            t.forward(50)
            t.left(170)
    t.end_fill()
    return


def shape2(side2):
    for i in range(10):
        t.forward(side2)
        for i in range(5):
            t.pencolor(randomcolor())
            t.right(30)
            t.forward(100)
            for i in range(2):
                t.pencolor("blue")
                t.right(70)
                t.forward(95)
                
    return
def origin():
    t.penup()
    t.goto(0,0)
    t.pendown()
    return
def atobe():
    for i in range(9):
        t.pencolor(randomcolor())
        for i in range(20):
            t.penup()
            t.goto(100,50)
            t.pendown()
            t.right(30)
            t.forward(150)
            t.goto(50,100)
    return

#TOP LEVEL
t.speed(0)  
#cool pattern def, random colors

coolpattern()

#color change for pen & spiral
t.pencolor("Blue")

origin()
t.penup()
t.forward(200)
t.pendown()


spiral()

origin()
t.penup()
t.left(70)
t.forward(150)
t.pendown()

#parametered drawing
side=input ("choose value between 1 to 50")
degree=input ("choose value from 1-360")
shape(side,degree)

origin()
t.penup()
t.right(90)
t.forward(300)
t.pendown()

#second parametered drawing
side2=input("choose value from 20-100")
shape2(side2)


origin()
t.penup()
t.right(30)
t.forward(400)
t.pendown()

#clock of colors - by shawn noruzi
atobe()
t.exitonclick()
