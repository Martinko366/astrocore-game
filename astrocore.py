import pygame, sys

from startup import Startup
from window import Game
from config import *

player_info = [True, 'Hero', 'Male']

try:
    player_info = Startup()
except NameError:
    exit(1)

g = Game(player_info)
g.new(LEVEL_DICT[CURRENT_LEVEL]['map'])
while g.running:
    g.main()

pygame.quit()
sys.exit()