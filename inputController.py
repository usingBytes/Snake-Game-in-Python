from turtle import Screen
# turtle heading info
# 0 - east
# 90 - north
# 180 - west
# 270 - south

class InputController:
    def __init__(self) -> None:
        screen = Screen() #singleton will find our other screen in main
        screen.listen()

        screen.onkey(key="w", fun=self.set_up)
        screen.onkey(key="s", fun=self.set_down)
        screen.onkey(key="a", fun=self.set_left)
        screen.onkey(key="d", fun=self.set_right)

        self.direction = 0

    def set_up(self):
        if (not self.direction == 270):
            self.direction = 90

    def set_down(self):
        if (not self.direction == 90):
            self.direction = 270

    def set_left(self):
        if (not self.direction == 0):
            self.direction = 180

    def set_right(self):
        if (not self.direction == 180):
            self.direction = 0

    def get_direction(self):
        return self.direction