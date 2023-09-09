import pygame, sys
from settings import *
from tile import Tile
from level import Level

#pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
# test_tile =Tile((100,100),64)
# test_tile_group = pygame.sprite.Group(test_tile)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('blue')
    level.run()
    # test_tile_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
