import pygame

# initialize pygame
pygame.init()

# create main screen
screen = pygame.display.set_mode((800, 600))

# main loop
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
