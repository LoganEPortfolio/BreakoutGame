from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        self.speed(0)
        self.goto(0, -180)
        
    
    def left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
        
    def right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())