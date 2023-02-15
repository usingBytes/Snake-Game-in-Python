import os

class FileManager:
    def __init__(self) -> None:
        self.directory = "YouTube/Projects/Snake Game in Python/score.txt"

    
    def read(self):
        highscore = 0

        if (os.path.exists(self.directory)):
            with open(self.directory, mode="r") as file:
                highscore = int(file.readline())
        return highscore

    
    def write(self, highscore):
        with open(self.directory, mode="w") as file:
            file.write(str(highscore))