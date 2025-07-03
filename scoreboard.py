from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} HIGH SCORE = {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if(self.score> self.high_score):
            self.high_score = Score
        self.score = 0
        self.update_score()
    #def game_over(self):
     #   self.goto(0,0)
     #   self.write("GAME OVER", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        
        self.score += 1
        
        self.update_score()