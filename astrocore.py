import pygame, sys

from startup import Startup
from window import Game

player_info = Startup()
print(player_info[0], player_info[1], player_info[2])

g = Game(player_info[2])
g.new()
while g.running:
    g.main()

pygame.quit()
sys.exit()