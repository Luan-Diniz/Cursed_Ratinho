import pygame
import sys

LENGTH = 887.9
WIDTH = 499.2

#Inicialization
pygame.init()
display = pygame.display.set_mode((LENGTH,WIDTH))
pygame.display.set_caption("Cursed Ratinho")

#Main loop
while True:
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #display update
    display.fill((255,255,255))
    pygame.display.update()
