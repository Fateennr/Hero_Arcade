import pygame
from tile import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):
        
        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        
    def setup_level(self,layout):
         self.tiles = pygame.sprite.Group()
         self.player1 = pygame.sprite.GroupSingle()
         for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x= col_index * tile_size
                y =row_index * tile_size
                
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                    
                if cell == 'P':
                    player = Player((x, y))
                    self.player1.add(player)
    
    def scroll_x(self):
        player1 = self.player1.sprite
        player1_x = player1.rect.centerx
        direction_x = player1.direction.x
        
        if player1_x <200:
            self.world_shift = 4
            player1.speed =0
               
    def run(self):
        #update tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #update player
        self.player1.update()
        self.player1.draw(self.display_surface)
        self.scroll_x()