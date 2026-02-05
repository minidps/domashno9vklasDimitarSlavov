import turtle
import random

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)

def draw_ground():
    t.penup()
    t.goto(-400, -300)
    t.setheading(0)
    t.fillcolor("white")
    t.begin_fill()
    
    t.pendown()
    t.forward(800)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(200)
    
    t.end_fill()

def draw_static_snow(count):
    t.penup()
    t.color("white")

    for _ in range(count):
        x = random.randint(-390, 390)
        y = random.randint(-50, 290)
        draw_circle("white", 2, x, y)

def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_triangle(color, x, y, width):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(width)
        t.left(120)
    t.end_fill()

def draw_tree(x, y):
    t.penup()
    t.goto(x - 10, y)
    t.setheading(0)
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

    draw_triangle("forestgreen", x - 50, y + 30, 100)
    draw_triangle("forestgreen", x - 40, y + 70, 80)
    draw_triangle("forestgreen", x - 30, y + 100, 60)

draw_ground()
draw_static_snow(120)

# Slunce
t.color("yellow")
draw_circle("yellow", 40, 250, 180)
t.penup()
t.color("yellow")
t.pensize(3)
for _ in range(12):
    t.penup()
    t.goto(290, 180)
    t.pendown()
    t.forward(80)
    t.right(30)

t.pensize(1)
t.color("black")

draw_tree(-150, -100)
draw_tree(150, -100)

# Snejen chovek
# Tqlo
draw_circle("white", 60, 0, -150)
draw_circle("white", 45, 0, -40)
draw_circle("white", 30, 0, 40)
# Ochi
draw_circle("black", 4, -10, 80)
draw_circle("black", 4, 10, 80)
# Nos
t.penup()
t.goto(0, 75)
t.setheading(0)
t.color("orange")
t.pendown()
t.begin_fill()
t.forward(15)
t.left(160)
t.forward(16)
t.end_fill()
# Kopcheta
draw_circle("black", 3, 0, -125)
draw_circle("black", 3, 0, -105)
draw_circle("black", 3, 0, -85)
draw_circle("black", 3, 0, -65)
draw_circle("black", 3, 0, -45)
draw_circle("black", 3, 0, -25)
draw_circle("black", 3, 0, -5)
draw_circle("black", 3, 0, 15)
draw_circle("black", 3, 0, 35)
# Usmivka
t.penup()
t.goto(-15, 70)
t.setheading(-60)
t.color("black")
t.pensize(2)
t.pendown()
t.circle(18, 120)
t.pensize(1)

# Ruce
t.color("saddlebrown")
t.pensize(3)
# Lqva ruka
t.penup()
t.goto(-40, 0)
t.setheading(150)
t.pendown()
t.forward(60)
# Prusti na lqvata ruka
t.backward(20)
t.left(45)
t.forward(15)
t.backward(15)
t.right(90)
t.forward(15)
# Dqsna ruka
t.penup()
t.goto(40, 0)
t.setheading(30)
t.pendown()
t.forward(50)
# Prusti na dqsnata ruka
t.backward(20)
t.right(45)
t.forward(15)
t.backward(15)
t.left(90)
t.forward(15)

# Metla
t.penup()
t.goto(90, -120)
t.setheading(95)
t.color("saddlebrown")
t.pensize(5)
t.pendown()
t.forward(180)
# Vetriloto na metlata
t.pensize(3)
t.right(45)
for i in range(11):
    if i % 2 == 0:
        t.color("goldenrod")
    else:
        t.color("yellow")
    
    t.forward(50)
    t.backward(50)
    t.left(10)

t.pensize(1)
t.color("black")

# Shapka
t.penup()
t.goto(-35, 95)
t.color("black")
t.setheading(0)
t.pendown()
t.begin_fill()
t.forward(70)
t.left(90)
t.forward(10)
t.left(90)
t.forward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)
t.end_fill()

t.hideturtle()
screen.mainloop()