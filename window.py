import pygame, pygame.camera, moviepy.editor
import sys, time

from config import *
from sprites import *

class Game:
    def __init__(self, fsc):
        pygame.init()
        pygame.mixer.init()
        pygame.camera.init()

        title_icon = pygame.image.load('resources/title/icon.png')
        pygame.display.set_caption('AstroCore')
        pygame.display.set_icon(title_icon)

        self.fullscreen = fsc
        if not self.fullscreen:
            self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
        elif self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.font = pygame.font.SysFont("Arial", 18)

        self.secret_intro = random.randint(1, 100)
        if self.secret_intro == 1:
            video = moviepy.editor.VideoFileClip("resources/cutscenes/intro2.mp4")
            video.preview()
        else:
            video = moviepy.editor.VideoFileClip("resources/cutscenes/intro.mp4")
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('resources/sounds/intro.mp3'), fade_ms=3000)
            pygame.mixer.Channel(0).set_volume(0.3)
            video.preview()

        self.character_spritesheet = Spritesheet('resources/img/character.png')
        self.terrain_spritesheet = Spritesheet('resources/img/terrain.png')
        self.floor_spritesheet = Spritesheet('resources/img/floor.png')
        self.border_spritesheet = Spritesheet('resources/img/border.png')

        self.overlay_img = pygame.image.load('resources/img/overlay.png').convert_alpha()
        self.black_screen = pygame.image.load('resources/img/blackscreen.png').convert_alpha()

        self.clock = pygame.time.Clock()
        self.running = True
        self.first_run = True

    def createTilemap(self):
        for i, row in enumerate(tilemap):
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

                if column == '1':
                    self.item = Item(self, j, i, 8, 32)

                # Player
                if column == 'P':
                    self.player = Player(self, j, i)

    def animateIn(self):
        time.sleep(0.5)
        self.black_screen.set_alpha(255)

        if self.secret_intro != 50:
            pygame.mixer.Channel(0).fadeout(3000)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sounds/background.mp3'), loops=-1, fade_ms=4000)
        pygame.mixer.Channel(1).set_volume(0.05)

        for i in range(255, 0, -1):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            self.screen.blit(self.overlay_img, (0, 0))

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)
        self.first_run = False

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        #self.enemies = pygame.sprite.LayeredUpdates()
        #self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

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

        if self.first_run:
            self.animateIn()

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False


    def game_over(self):
        pass

    def intro_screen(self):
        pass