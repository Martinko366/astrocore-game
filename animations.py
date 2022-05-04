import pygame, time, random, math

from config import *
import config

class Animate:
    def overlayStatus_texts(self):
        self.drawText(f'Health: {int(config.HP)}%', 42, DARKGREEN, 10, 30)
        self.drawText(f'Energy: {int(config.STAMINA)}%', 42, DARKGREEN, 10, 60)

        self.drawText(f'{config.COINS}A$ * {config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 32, DARKGREEN, 10, 130)


    def newLevel_animateIn(self):
        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            font = pygame.font.Font("resources/font/NoizeSportFreeVertionRegular.ttf", 42)
            text_surf = font.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 500))

            text_surf.set_alpha(i)
            self.screen.blit(text_surf, text_rect)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(1)
        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            font = pygame.font.Font("resources/font/NoizeSportFreeVertionRegular.ttf", 42)
            text_surf = font.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 500))
            self.screen.blit(text_surf, text_rect)

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 38)
            text_surf = font.render(str(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}'), True,
                                    (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 560))

            text_surf.set_alpha(i)
            self.screen.blit(text_surf, text_rect)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(2)
        for i in range(255, 0, -5):
            self.screen.fill(BLACK)

            font = pygame.font.Font("resources/font/NoizeSportFreeVertionRegular.ttf", 42)
            text_surf1 = font.render(str('You found new location!'), True, (30, 135, 61)).convert_alpha()
            text_rect1 = text_surf1.get_rect(center=(1920 // 2, 500))

            font = pygame.font.Font("resources/font/Pixellettersfull-BnJ5.ttf", 38)
            text_surf = font.render(str(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}'), True,
                                    (30, 135, 61)).convert_alpha()
            text_rect = text_surf.get_rect(center=(1920 // 2, 560))

            text_surf.set_alpha(i)
            text_surf1.set_alpha(i)
            self.screen.blit(text_surf, text_rect)
            self.screen.blit(text_surf1, text_rect1)

            pygame.display.update()
            time.sleep(0.0005)


    def screen_animateOut(self):
        time.sleep(0.1)
        self.black_screen.set_alpha(0)

        for i in range(0, 255, 5):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            self.screen.blit(self.overlay_img, (0, 0))

            self.a.overlayStatus_texts()

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)


    def screen_animateIn(self):
        time.sleep(0.1)
        self.black_screen.set_alpha(255)

        for i in range(255, 0, -5):
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.clock.tick(FPS)
            self.screen.blit(self.overlay_img, (0, 0))

            self.game.overlay_text

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)
        self.first_run = False