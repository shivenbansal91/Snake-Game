from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt") as file:
            self.high_score =  int(file.read())
        
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} HIGH SCORE = {self.high_score}", align=ALIGNMENT, font= FONT)

    def reset(self):
        if(self.score> self.high_score):
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
                
            
        self.score = 0
        self.update_score()
    #def game_over(self):
     #   self.goto(0,0)
     #   self.write("GAME OVER", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        
        self.score += 1
        
        self.update_score()