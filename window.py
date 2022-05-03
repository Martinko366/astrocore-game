import random

import pygame, moviepy.editor
from pypresence import Presence
import sys, time

import config
from config import *
from sprites import *

class Game:
    def __init__(self, player_data):
        pygame.init()
        pygame.mixer.init()

        try:
            self.DP = Presence('920391194515746856')
            self.DP.connect()
        except:
            pass

        self.start_ts = time.time()

        title_icon = pygame.image.load('resources/title/icon.png')
        pygame.display.set_caption('AstroCore')
        pygame.display.set_icon(title_icon)

        PLAYER_NAME = player_data[1]
        PLAYER_SEX = player_data[2]

        self.fullscreen = player_data[0]
        if not self.fullscreen:
            self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
        elif self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.secret_intro = random.randint(1, 100)
        if self.secret_intro == 1:
            video = moviepy.editor.VideoFileClip("resources/cutscenes/intro2.mp4")
            video.preview()
        else:
            video = moviepy.editor.VideoFileClip("resources/cutscenes/intro.mp4")
            video.preview()

        self.character_spritesheet = Spritesheet('resources/img/character.png')
        self.terrain_spritesheet = Spritesheet('resources/img/terrain.png')
        self.floor_spritesheet = Spritesheet('resources/img/floor.png')
        self.border_spritesheet = Spritesheet('resources/img/border.png')

        self.coin_texture = Spritesheet('resources/img/coin.png')

        self.overlay_img = pygame.image.load('resources/img/overlay.png').convert_alpha()
        self.black_screen = pygame.image.load('resources/img/blackscreen.png').convert_alpha()

        self.clock = pygame.time.Clock()
        self.running = True

        self.first_run = True
        self.music_run = False

    def drawText(self, text, size, color, x, y):
        font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", size)

        text_surf = font.render(str(text), True, color)
        text_rect = text_surf.get_rect(x=x, y=y)

        self.screen.blit(text_surf, text_rect)

    def createTilemap(self, level):
        for i, row in enumerate(level):
            if self.fullscreen:
                i += 10
            for j, column in enumerate(row):
                if self.fullscreen:
                    j += 10
                Ground(self, j, i)

                # Void
                if column == ' ':
                    self.block = Void(self, j, i)

                # Borders
                if column == 'B':
                    self.block = Border(self, j, i, 160, 0)
                if column == 'b':
                    self.block = Border(self, j, i, 160, 320)
                if column == 'N':
                    self.block = Border(self, j, i, 32, 64)
                if column == 'n':
                    self.block = Border(self, j, i, 288, 64)

                # Border Corners
                if column == 'M':
                    self.block = Border(self, j, i, 256, 0)
                if column == 'm':
                    self.block = Border(self, j, i, 256, 320)
                if column == 'V':
                    self.block = Border(self, j, i, 64, 0)
                if column == 'v':
                    self.block = Border(self, j, i, 32, 288)

                if column == 'C':
                    self.block = Border(self, j, i, 64, 32)
                if column == 'c':
                    self.block = Border(self, j, i, 256, 32)
                if column == 'X':
                    self.block = Border(self, j, i, 312, 32)
                if column == 'x':
                    self.block = Border(self, j, i, 8, 32)

                # Border Endings
                if column == 'Z':
                    self.block = Border(self, j, i, 448, 224)
                if column == 'z':
                    self.block = Border(self, j, i, 384, 96)

                # Coins
                if column == '.':
                    try:
                        if COINS > 300:
                            randNum = 30
                        else:
                            randNum = 50
                    except:
                        randNum = 30
                    if random.randint(1,randNum) == 3:
                        self.coin = Coin(self, j, i)

                # Level Teleport
                if column == '1' or column == '2':
                    self.item = Teleport(self, j, i)

                # Player
                if column == 'P':
                    self.player = Player(self, j, i)

    def animateIn_level(self):
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('resources/sounds/alert.wav'))

        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 42)
            text_surf = font.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 500))

            text_surf.set_alpha(i)
            self.screen.blit(text_surf, text_rect)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(1)
        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 42)
            text_surf = font.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 500))
            self.screen.blit(text_surf, text_rect)

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 36)
            text_surf = font.render(str(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}'), True,
                                    (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 540))

            text_surf.set_alpha(i)
            self.screen.blit(text_surf, text_rect)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(2)
        for i in range(255, 0, -5):
            self.screen.fill(BLACK)

            font1 = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 42)
            text_surf1 = font1.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect1 = text_surf1.get_rect(center=(1920 // 2, 500))

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 36)
            text_surf = font.render(str(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}'), True,
                                    (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 540))

            text_surf.set_alpha(i)
            text_surf1.set_alpha(i)
            self.screen.blit(text_surf, text_rect)
            self.screen.blit(text_surf1, text_rect1)

            pygame.display.update()
            time.sleep(0.0005)

    def animateOut(self):
        time.sleep(0.1)
        self.black_screen.set_alpha(0)

        for i in range(0, 255, 5):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            self.screen.blit(self.overlay_img, (0, 0))

            self.drawText(f'HP: {int(config.HP)}', 42, DARKGREEN, 10, 10)
            self.drawText(f'Stamina: {int(config.STAMINA)}', 42, DARKGREEN, 10, 40)

            self.drawText(f'Location: {config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 32, DARKGREEN, 10, 110)
            self.drawText(f'Coins on you: {config.COINS}', 32, DARKGREEN, 10, 140)

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)

    def animateIn(self):
        time.sleep(0.1)
        self.black_screen.set_alpha(255)

        for i in range(255, 0, -5):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            self.screen.blit(self.overlay_img, (0, 0))

            self.drawText(f'HP: {int(config.HP)}', 42, DARKGREEN, 10, 10)
            self.drawText(f'Stamina: {int(config.STAMINA)}', 42, DARKGREEN, 10, 40)

            self.drawText(f'Location: {config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 32, DARKGREEN, 10, 110)
            self.drawText(f'Coins on you: {config.COINS}', 32, DARKGREEN, 10, 140)

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)
        self.first_run = False

    def new(self, level):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        #self.enemies = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()
        self.coinsl = pygame.sprite.LayeredUpdates()
        self.teleport = pygame.sprite.LayeredUpdates()

        self.createTilemap(level)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)

        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        self.screen.blit(self.overlay_img, (0, 0))

        self.drawText(f'HP: {int(config.HP)}', 42, DARKGREEN, 10, 10)
        self.drawText(f'Stamina: {int(config.STAMINA)}', 42, DARKGREEN, 10, 40)

        self.drawText(f'Location: {config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 32, DARKGREEN, 10, 110)
        self.drawText(f'Coins on you: {config.COINS}', 32, DARKGREEN, 10, 140)

        if not config.LEVEL_DICT[config.CURRENT_LEVEL]['found']:
            self.animateIn_level()

        if self.first_run:
            if not self.music_run:
                pygame.mixer.Channel(1).play(
                    pygame.mixer.Sound(f'resources/sounds/{config.LEVEL_DICT[config.CURRENT_LEVEL]["music"]}.wav'),
                    loops=-1, fade_ms=2000)
                pygame.mixer.Channel(1).set_volume(0.4)
                self.music_run = True
                self.first_run = False
            self.animateIn()

            config.LEVEL_DICT[config.CURRENT_LEVEL]['found'] = True

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def discord_presence(self):
        print(self.DP.update(state="Astrocore",
                             details="Wondering in spaceship"))

    def game_over(self):
        pass