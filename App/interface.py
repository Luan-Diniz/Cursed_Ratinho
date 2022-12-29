import pygame
import sys
import re
from screeninfo import get_monitors

resolucao = ''

for m in get_monitors():
    resolucao = str(m)
    
resolucao_altura = re.findall('width=.+?,', resolucao)
resolucao_altura = resolucao_altura[0]
resolucao_altura = str(resolucao_altura)
resolucao_altura = resolucao_altura.replace('width=', '')
resolucao_altura = resolucao_altura.replace(',', '')
resolucao_altura = float(resolucao_altura)*0.65

resolucao_largura = re.findall('height=.+?,', resolucao)
resolucao_largura = resolucao_largura[0]
resolucao_largura = str(resolucao_largura)
resolucao_largura = resolucao_largura.replace('height=', '')
resolucao_largura = resolucao_largura.replace(',', '')
resolucao_largura = float(resolucao_largura)*0.65

#Inicialization
pygame.init()
display = pygame.display.set_mode((resolucao_altura,resolucao_largura))
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
