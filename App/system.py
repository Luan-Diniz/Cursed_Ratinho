import pygame
import sys

class Control:
    def __init__(self,largura,altura):
        self.__screen_width = largura * 0.65
        self.__screen_height = altura * 0.65
        self.__interface_logic = {'first_menu' : True,      #Used to control interface
                                  'config_menu': False,
                                  'running' : False,}

        # Inicialization
        pygame.init()
        pygame.display.set_caption("Cursed Ratinho")
        self.__display = pygame.display.set_mode((self.__screen_width, self.__screen_height))

    def start(self):
        #Main loop
        while True:
            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #display update
            self.__display.fill((255,255,255))
            pygame.display.update()
