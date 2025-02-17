from turtle import Turtle

align = "center"
fonts = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", False, align= align, font= fonts)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.", False, align= align, font= fonts)


    def points(self):
        self.score += 1
        self.clear()
        self.update_score()
