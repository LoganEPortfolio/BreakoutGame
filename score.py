from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.score, align='center', font=('Courier', 40, 'normal'))
        
    def add_points(self):
        self.score += 100
        self.update_score()
        