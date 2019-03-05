# coding pong according to freecodecamp.org

import turtle
import random
import math
import time

# Parameters
width = 800
height = 600
absspeed = 200
FOV = 0.5
lastFrameTime = time.time()
deltaTime = 0
bFirstRun = True


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
ball.lastPos = [ball.xcor(), ball.ycor()]


# Functions

def newBallAngle():
    # alpha in range 45 degree till 135 degree
    # alpha in range pi/4 till 3*pi/4
    alpha = math.pi/2 + random.uniform(-FOV*math.pi/2, FOV*math.pi/2)
    return [math.sin(alpha) * absspeed, math.cos(alpha) * absspeed]

[ball.dx, ball.dy] = newBallAngle()

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

def moveBall(lastFrameTime):
    # Moves the ball with a normalized step
    if not bFirstRun:
        deltaTime = time.time() - lastFrameTime
        lastFrameTime = time.time()
        ball.setx(ball.xcor() + deltaTime*ball.dx)
        ball.sety(ball.ycor() + deltaTime*ball.dy)
    else:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    return lastFrameTime

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




# Main game loop
while True:
    wn.update()

    # check actual speed of ball

    dt = time.time() - lastFrameTime
    lastFrameTime = moveBall(lastFrameTime)
    dx =  ball.xcor() - ball.lastPos[0]
    dy =  ball.ycor() - ball.lastPos[1]
    print( (dx**2 + dy**2) / dt**2 )
    ball.lastPos = [ball.xcor(), ball.ycor()]
    bFirstRun = False


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

        [ball.dx, ball.dy] = newBallAngle()
        print(ball.dx**2 + ball.dy**2)
        ball.dx *= -1

    if ball.xcor() <= -(width/2-10):
        ball.goto(0,0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
            align="center", font=("Courier", 24, "normal"))
        [ball.dx, ball.dy] = newBallAngle()


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
