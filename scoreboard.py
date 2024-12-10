from turtle import Turtle  # we want to create shape because of that we use the Turtle class

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color('White')
        self.penup()
        self.goto(0,270)
        self.write(f'score = {self.score}',align='center',font=('Arial',24,"normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'score = {self.score}', align='center', font=('Arial', 24, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align='center', font=('Arial', 24, "normal"))

