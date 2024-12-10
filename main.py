from  turtle import   Screen
import time
from snake import Snake
from food import Food
from  scoreboard import  Scoreboard

screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn turtle animation off.and we use this with update method to turn on the animation

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen() #listen to  get input key from keyboard
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()  # update the screen to show the movement of each square
    time.sleep(0.1)  # set 0.1 time delay between each movement of 3 square together
    snake.move()

    #Detsct collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detsct collision with wall
    if snake.head.xcor()>280 or  snake.head.xcor()<-280 or  snake.head.ycor()>280 or  snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #Detsct collision with tail
    for segment in snake.segment[1:]:  #if Head collides with any segment in the tail
        if snake.head.distance(segment) <10 :
            game_is_on=False
            scoreboard.game_over()
screen.exitonclick()