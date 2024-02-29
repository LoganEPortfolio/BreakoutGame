from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = random.choice([-2,2])
        self.y_move = 2
        self.move_speed = 0.2
        self.lives = 3
        
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
       
       
    def check_border_collision(self):
        if self.xcor() > 280 or self.xcor() < -280:
            self.x_move *= -1
        if self.ycor() > 280:
            self.y_move *= -1   
       
    def check_player_collision(self, player):
        ball_x, ball_y = self.position()
        player_x, player_y = player.position()
        if ball_y - 10 < player_y + 25 and \
            ball_x > player_x - 50 and ball_x < player_x + 50:
                self.y_move *= -1

    def reset_ball(self):
        self.lives -= 1
        self.update_lives()
        print(self.lives)
        self.goto(0, 20)

    def update_lives(self):
        self.clear()
        self.goto(150, 200)
        self.write(self.lives, align='center', font=('Courier', 40, 'normal'))