from turtle import Turtle


class Bars(Turtle):
    def __init__(self, x, y ,color):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.shapesize(stretch_len=2, stretch_wid=0.5)
        
        
        

            
