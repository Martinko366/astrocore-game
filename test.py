import pygame
import time

pygame.init()

display_size = pygame.display.Info().current_w , pygame.display.Info().current_h - 50
screen = pygame.display.set_mode(display_size)
image = pygame.image.load('resources/title/icon.png')
image_size = image.get_rect().size

centered_image = [(display_size[0] - image_size[0])/2, (display_size[1] - image_size[1])/2]

time.sleep(1)


def animate():
    global screen
    global image

    for i in range (255):
        screen.fill((0,0,0))
        image.set_alpha(i)
        screen.blit(image, centered_image)
        pygame.display.update()
        time.sleep(0.001)

    time.sleep(1.5)

    for i in range (255, 0, -1):
        screen.fill((0,0,0))
        image.set_alpha(i)
        screen.blit(image, centered_image)
        pygame.display.update()
        time.sleep(0.001)

    time.sleep(1.5)

    animate()


animate()