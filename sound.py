import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'glock.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'glock.wav')
        self.npc_shot.set_volume(0.2)
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.3)