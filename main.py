from turtle import Screen,Turtle
import time
from score import Scoreboard
from snake import Snake
from food import Food

screen=Screen()
screen.setup(600,600)
screen.bgcolor("skyblue")
screen.title("Anaconda")
screen.tracer(0)
food=Food()
score = Scoreboard()
score.getting_name()



snake=Snake()
screen.listen()
screen.onkey(key="Up",fun=snake.go_up)
screen.onkey(key="Down",fun=snake.go_down)
screen.onkey(key="Right",fun=snake.go_right)
screen.onkey(key="Left",fun=snake.go_left)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if(snake.head.distance(food)<30):
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        game_is_on =False
        score.game_over()
    for segment in snake.segments:
        if segment ==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()


screen.exitonclick()