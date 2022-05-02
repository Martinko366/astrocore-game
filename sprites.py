import pygame
import random
import math

from window import *
from config import *
import config


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
        self.current_level = CURRENT_LEVEL

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()
        self.collide_teleport()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.collide_coin('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.collide_coin('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()

        ADD_PLAYER_SPEED = 0

        if config.STAMINA > 1:
            if keys[pygame.K_LSHIFT]:
                ADD_PLAYER_SPEED = 4
                config.STAMINA -= 1
        if not keys[pygame.K_LSHIFT]:
            if config.STAMINA < 100:
                if random.randint(1,8) == 3:
                    config.STAMINA += 1


        if keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED + ADD_PLAYER_SPEED
            self.y_change -= PLAYER_SPEED + ADD_PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED + ADD_PLAYER_SPEED
            self.y_change += PLAYER_SPEED + ADD_PLAYER_SPEED
            self.facing = 'down'
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED + ADD_PLAYER_SPEED
            self.x_change -= PLAYER_SPEED + ADD_PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED + ADD_PLAYER_SPEED
            self.x_change += PLAYER_SPEED + ADD_PLAYER_SPEED
            self.facing = 'right'


    def collide_teleport(self):
        tp_hits = pygame.sprite.spritecollide(self, self.game.teleport, False)

        if tp_hits:
            if LEVEL_DICT[config.CURRENT_LEVEL]['goto'][self.facing] == '':
                config.CURRENT_LEVEL = 'lobby'
            else:
                config.CURRENT_LEVEL = LEVEL_DICT[config.CURRENT_LEVEL]['goto'][self.facing]

            new_level_map = LEVEL_DICT[config.CURRENT_LEVEL]['map']

            self.game.first_run = True
            self.game.animateOut()
            self.game.new(new_level_map)

    def collide_coin(self, direction):
        if direction == 'x' or direction == 'y':
            coin_hits = pygame.sprite.spritecollide(self, self.game.coinsl, True)
            if coin_hits:
                config.COINS += random.randint(5, 20)

    def collide_blocks(self, direction):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LSHIFT]:
            ADD_PLAYER_SPEED = 2
        if not keys[pygame.K_LSHIFT]:
            ADD_PLAYER_SPEED = 0

        if direction == 'x':
            block_hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if block_hits:
                if self.x_change > 0:
                    self.rect.x = block_hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED + ADD_PLAYER_SPEED
                if self.x_change < 0:
                    self.rect.x = block_hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED + ADD_PLAYER_SPEED

        if direction == 'y':
            block_hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if block_hits:
                if self.y_change > 0:
                    self.rect.y = block_hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED + ADD_PLAYER_SPEED
                if self.y_change < 0:
                    self.rect.y = block_hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED + ADD_PLAYER_SPEED

    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


class Border(pygame.sprite.Sprite):
    def __init__(self, game, x, y, first, last):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.border_spritesheet.get_sprite(first, last, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Coin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ITEM_LAYER
        self.groups = self.game.all_sprites, self.game.coinsl
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(448, 224, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.graund = 0
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.floor_spritesheet.get_sprite(194, 341, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Teleport(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ITEM_LAYER
        self.groups = self.game.all_sprites, self.game.teleport
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(224, 736, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Void(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y