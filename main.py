from turtle import Screen
import time
from player import Player
from blocks import Bars
from ball import Ball
import random


class Game: 
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title("Breakout")

        self.player = Player()
        self.ball = Ball()
        self.blocks = []
        self.create_blocks()

        self.screen.listen()
        self.screen.onkeypress(fun=self.player.left, key="Left")
        self.screen.onkeypress(fun=self.player.right, key="Right")

    def create_blocks(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        for y in range(270, 60, -20):
            for x in range(-280, 280, 40):
                block = Bars(x, y, random.choice(colors))
                self.blocks.append(block)


    def main_loop(self):
        while True:
            self.screen.update()
            
            self.ball.move_ball()
            self.ball.check_border_collision()
            self.ball.check_player_collision(self.player)
            
            for block in self.blocks:
                if self.ball.distance(block) < 20:
                    self.ball.x_move *= -1
                    block.hideturtle()
                    self.blocks.remove(block)
                    if not self.blocks:
                        print("Game Over")
                        break


if __name__ == "__main__":
    game = Game()
    game.main_loop()


