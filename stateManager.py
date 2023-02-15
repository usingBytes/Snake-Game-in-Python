class StateManager:
    def __init__(self)->None:
        self.is_playing = True
        self.is_gameover = False
        self.is_newgame = True
        self.is_dead = False

    def get_is_playing(self):
        return self.is_playing

    def set_is_playing(self, value):
        self.is_playing = value

    def get_is_gameover(self):
        return self.is_gameover

    def set_is_gameover(self, value):
        self.is_gameover = value
    
    def get_is_newgame(self):
        return self.is_newgame

    def set_is_newgame(self, value):
        self.is_newgame = value
    
    def get_is_dead(self):
        return self.is_dead

    def set_is_dead(self, value):
        self.is_dead = value