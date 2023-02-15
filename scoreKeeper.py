from turtle import Turtle
import os

class ScoreKeeper(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()

    
    def get_score(self):
        return self.score

    def set_score(self):
        self.score += 100

    def get_highscore(self):
        return self.highscore

    def set_highscore(self, value):
        self.highscore = value

    def update(self):
        if (self.score > self.highscore):
            self.highscore = self.score

        self.clear()
        
        # SCORE
        self.penup()
        self.goto(-275, 260)
        self.pendown()
        self.write(f"Score: {self.get_score()}", font=("Arial", 14, "normal"))

        # HIGH SCORE
        self.penup()
        self.goto(-275, 240)
        self.pendown()
        self.write(f"High Score: {self.get_highscore()}", font=("Arial", 14, "normal"))