from sprite_object import *
from npc import *
import random
from random import choice, randrange
from map import mini_map
class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        #npc settings
        self.enemies = random.randint(5,10)
        
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()
        self.spawn_sprite()


        #sprite map
        #add_sprite(SpriteObject(game))

    def spawn_sprite(self):
        for i in range(6):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
        self.add_sprite(AnimatedSprite(self.game, pos=(x+0.5, y+0.5)))
        
        
        for i in range(6):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
        self.add_sprite(SpriteObject(self.game, path=self.static_sprite_path + 'table2.png', pos=(x+0.5, y+0.5)))

        #npc map
    def spawn_npc(self):
        for i in range(self.enemies):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)

            self.add_npc(NPC(self.game, pos=(x+0.5,y+0.25)))
        
        #add_npc(NPC(game))
        #add_npc(NPC(game, pos=(10,9)))
        #add_npc(NPC(game, pos=(10,8)))
        #add_npc(NPC(game, pos=(8,10), path='resources/sprites/npc/npc2/0.png'))
        #add_npc(NPC(game, pos=(8,11), path='resources/sprites/npc/npc2/0.png'))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
        

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
