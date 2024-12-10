from  turtle import  Turtle, Screen

import select

STARTING_POSITION=((0,0),(-20,0),(-40,0))
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0] #the first square

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # invisible the pen color while moving to next position
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())  #.position() ==> return a position of snake tail

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # start=len , stop=0, step=-1
            new_x = self.segment[seg_num - 1].xcor()  # return x,y position of front square
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)  # set each previous square with location of front square
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN: #return the direction of the first square
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)




