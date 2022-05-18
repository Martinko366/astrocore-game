import pygame, moviepy.editor, sys

from startup import Startup
from window import Game
from config import *

player_info = [True, 'Hero', 'Male']
startupDone = False

try:
    player_info = Startup()
    startupDone = True
except Exception:
    exit(1)

if startupDone:
    video = moviepy.editor.VideoFileClip("resources/cutscenes/loading1.mp4")
    video.preview()

g = Game(player_info)
g.new(LEVEL_DICT[CURRENT_LEVEL]['map'])
while g.running:
    g.main()

pygame.quit()
sys.exit()