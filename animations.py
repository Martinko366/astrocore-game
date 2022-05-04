import pygame, time, random, math

from config import *
import config

class Animate:
    def overlayStatus_texts(self):
        self.drawText(f'{config.PLAYER_NAME}', 40, DARKGREEN, 10, 1, config.FONT2)

        self.drawText(f'Health: {int(config.HP)}%', 42, DARKGREEN, 10, 60)
        self.drawText(f'Energy: {int(config.STAMINA)}%', 42, DARKGREEN, 10, 90)

        self.drawText(f'{config.COINS}A$   *   {config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 32, DARKGREEN, 10, 140)


    def newLevel_animateIn(self):
        width = 1920 // 2

        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            self.drawText('You found new location!', 42, DARKGREEN, width, 500, config.FONT2, i)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(1)
        for i in range(0, 255, 5):
            self.screen.fill(BLACK)

            self.drawText('You found new location!', 42, DARKGREEN, width, 500, config.FONT2)
            self.drawText(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 38, DARKGREEN, width, 560, config.FONT1, i)

            pygame.display.update()
            time.sleep(0.0005)
        time.sleep(2)
        for i in range(255, 0, -5):
            self.screen.fill(BLACK)

            self.drawText('You found new location!', 42, DARKGREEN, width, 500, config.FONT2, i)
            self.drawText(f'{config.LEVEL_DICT[config.CURRENT_LEVEL]["title"]}', 38, DARKGREEN, width, 560, config.FONT1, i)

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

            self.a.overlayStatus_texts(self)

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

            self.a.overlayStatus_texts(self)

            self.black_screen.set_alpha(i)
            self.screen.blit(self.black_screen, (0, 0))
            pygame.display.update()
            time.sleep(0.00005)
        self.screen.blit(self.black_screen, (0, 0))
        self.black_screen.set_alpha(100)
        self.first_run = False