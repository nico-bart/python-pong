# coding pong according to freecodecamp.org

import turtle
import random

width = 800
height = 600
wn = turtle.Screen()
wn.title("Pong by Nico")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0) # manually updating



# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("lightblue")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 0.5
ball.dy = 1.2

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



# Functions
def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collisions
    if ball.ycor() >= (height/2-10):
        ball.sety(height/2-10)
        ball.dy *= -1

    if ball.ycor() <= -(height/2-10):
        ball.sety(-(height/2-10))
        ball.dy *= -1

    if ball.xcor() >= (width/2-10):
        ball.goto(0,0)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
            align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    if ball.xcor() <= -(width/2-10):
        ball.goto(0,0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
            align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    # Paddle collisions
    # Paddle A
    if (ball.xcor() < -340 and
        ball.xcor() > -345 and
        ball.ycor() < paddle_a.ycor()+40 and
        ball.ycor() > paddle_a.ycor()-40 ):
        ball.dx *= -1

    # Paddle B
    if (ball.xcor() > 340 and
        ball.xcor() < 345 and
        ball.ycor() < paddle_b.ycor()+40 and
        ball.ycor() > paddle_b.ycor()-40 ):
        ball.dx *= -1
