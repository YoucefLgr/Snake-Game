from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)
tt = Snake()
s = Score()
f = Food()
sc.listen()
sc.onkey(tt.left, "Left")
sc.onkey(tt.right, "Right")
sc.onkey(tt.up, "Up")
sc.onkey(tt.down, "Down")

t = True
while t:
    time.sleep(0.1)
    sc.update()
    tt.move()
    if tt.turtles[0].distance(f) < 15:
        f.refresh()
        tt.extend()
        s.increase()
    if tt.turtles[0].xcor() > 280 or tt.turtles[0].xcor() < -280 or tt.turtles[0].ycor() > 280 or \
            tt.turtles[0].ycor() < -280:
        tt.reset()
        s.hi()
    for _ in tt.turtles:
        if _ == tt.turtles[0]:
            pass
        elif _.distance(tt.turtles[0]) < 10:
            tt.reset()
            s.hi()

    sc.update()

sc.exitonclick()
