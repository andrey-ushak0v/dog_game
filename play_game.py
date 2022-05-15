import pygame
import sys

def start():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('cosmo_wars')
    color = (9, 3, 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(color)
        pygame.display.flip()

start()
