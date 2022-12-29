import pygame
import sys
from screeninfo import get_monitors

#Get screen size
screen_height, screen_width = 0, 0
for monitor in get_monitors():
    if  monitor.is_primary:
        screen_height = monitor.height
        screen_width = monitor.width
if screen_height == 0 or screen_width == 0:
    raise Exception("No primary monitor set: Unable to get the size.")

#Inicialization
pygame.init()
display = pygame.display.set_mode((screen_width * 0.65, screen_height * 0.65))
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
