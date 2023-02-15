from turtle import Turtle
import random

class FruitDispenser(Turtle):
    def __init__(self, bounds) -> None:
        super().__init__()

        self.is_available = False
        self.shape("circle")
        self.colors = ["yellow", "blue", "green", "red", "pink", "orange"]
        self.color(random.choice(self.colors))
        self.shapesize(0.5, 0.5)
        self.setheading(90)
        self.hideturtle()

        self.spawn(bounds)

    
    def spawn(self, bounds):
        bounds = bounds - 40 # I DONT WANT FOOD SPAWN ON IMMEDIATE EDGE
        if (not self.is_available):
            self.penup()
            self.goto(random.randrange(-bounds, bounds, 20), random.randrange(-bounds, bounds, 20))
            self.color(random.choice(self.colors))
            self.showturtle()
            self.is_available = True

    
    # check distance from segment[0] and "eat" if we collide
    # return true/false we will use this return to see if we grow larger
    def eat(self, position, bounds):
        distance = self.distance(position)
        if (distance <= 15):
            self.hideturtle()
            self.is_available = False
            self.spawn(bounds)
            return True
        else:
            return False