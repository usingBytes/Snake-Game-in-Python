from turtle import Screen
import time
from stateManager import StateManager
from inputController import InputController
from snake import Snake
from fruitDispenser import FruitDispenser
from scoreKeeper import ScoreKeeper
from fileManager import FileManager

#   Snake Game in Python using Turtle Graphics
#   Description:
#       The player controls a snake while trying to pickup food.
#       If the snake goes out of the game area, or collides with itself, the game is over.
#       Game difficulty is increased every time the player eats some food, as the snakes body grows longer
#   Turtle Graphics Documentation: https://docs.python.org/3/library/turtle.html
#   GitHub Source Code: https://github.com/usingBytes
#   
#   Let me know in the comments if the font size is large enough (or too big), and if the volume is at an ok level... Thanks!

BOUNDS = 300

screen = Screen()
state_manager = StateManager()
file_manager = FileManager()

def check_bounds(x, y):
    if (x <= -BOUNDS or x >= BOUNDS or y >= BOUNDS or y <= -BOUNDS):
        return True

while (state_manager.get_is_playing() and not state_manager.get_is_gameover()):
    time.sleep(0.1)

    # GAME INITIALIZATION
    if (state_manager.get_is_newgame()):
        screen.clear()
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.tracer(0)

        score_keeper = ScoreKeeper()

        # LOAD HIGH SCORE
        score_from_disk = file_manager.read()
        if (score_from_disk > score_keeper.get_highscore()):
            score_keeper.set_highscore(score_from_disk)
        
        input_controller = InputController()
        fruit_dispenser = FruitDispenser(BOUNDS)
        snake = Snake()

        state_manager.set_is_newgame(False)

    # CONTINUE PLAYING || QUIT
    # UPDATE SCORES
    elif (state_manager.get_is_dead()):
        if (score_keeper.get_highscore() > file_manager.read()):
            file_manager.write(score_keeper.get_highscore())

        play_again = screen.textinput("You Died!", "Play Again? 'Y'||'N'")

        if (play_again.lower() == "y"):
            state_manager.set_is_newgame(True)
            state_manager.set_is_dead(False)
        elif (play_again.lower() == "n"):
            state_manager.set_is_gameover(True)

    # CORE LOOP
    else:
        if (check_bounds(snake.get_segments()[0].xcor(), snake.get_segments()[0].ycor())):
            state_manager.set_is_dead(True)

        if (snake.check_collision(input_controller.get_direction())):
            state_manager.set_is_dead(True)

        snake.move(input_controller.get_direction())

        if (fruit_dispenser.eat(snake.get_segments()[0].position(), BOUNDS)):
            snake.add_segment(input_controller.get_direction())
            score_keeper.set_score()

        score_keeper.update()

    screen.update()
else:
    quit()

#TODO   create our window
#TODO   create our game loop
#TODO   create a state manager
#TODO   create our base snake (head + 2 body segments)
#TODO   make our snake move
#TODO   add input controls
#TODO   define our game area / collision detection
#TODO   spawn fruit
#TODO   make fruit edible
#TODO   create func for our snake to grow +1 segment whenever we eat food
#TODO   we need to check collision with ourself
#TODO   but we also need to make it so we dont accidently collide with ourself
#TODO   track our score and highscore values - +100 points everytime we eat food
#TODO   display scores
#TODO   read/write our highscore value to a .txt file, that we can use when loading up the game too

#   CLASSES
#       Usually I would take the time to plan out the systems, using diagrams etc
#       This is pretty simple, so we will just think about it for a moment looking at the TODO list
#
#       main - entry point / game loop
#       stateManager - the different game states we can be in (game over, new game etc)
#       snake - our snake obj
#       scoreKeeper
#       fruitDispenser
#       inputController
#       fileManager        