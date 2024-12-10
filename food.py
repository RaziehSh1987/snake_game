from  turtle import Turtle
import  random as rnd
class Food(Turtle):
    def __init__(self):
        super().__init__() #inheriant from the turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #circle 10 by 10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x=rnd.randint(-280,280)
        random_y=rnd.randint(-280,280)
        self.goto(random_x,random_y)


