import pygame
import time
import random

import sys

from Functions.simple_functions import *
from Functions.Menu import menu_loop

pygame.init()
pygame.display.set_caption('Project Enigma')
clock=pygame.time.Clock() 

def game_loop():
    
    menu = False
    GameExit = False
    while not GameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #message_display(text,x,y,color,font='freesansbold.ttf',size=30) 

        
        gameDisplay.fill(blue)
        message_display("Hehe tu nic nie ma",(display_width*0.6),(display_height*0.5),green) 
        
        gameDisplay.blit(main_char,(display_width*0.4,display_height*(0.05)))
        pygame.display.update()
                   
        clock.tick(60)
menu_loop()
game_loop()

pygame.quit()
quit()