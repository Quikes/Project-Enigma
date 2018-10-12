import pygame
import time
import random

import sys

from Functions.simple_functions import *

from Functions.Menu import menu_loop
from Functions import Menu

    

""" pygame.key.set_repeat (50, 30) """  
pygame.init()
pygame.display.set_caption('Project Enigma')
pygame.HWSURFACE|pygame.DOUBLEBUF
clock=pygame.time.Clock() 
#dodałem koentarz
def game_loop():
    
    main_character=Menu.mch()
    player = Player(400,500,main_character)
    blocky = Platform(600,400,200,100,black)
    menu = False
    GameExit = False
    while not GameExit: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            player.move(event)
           
        
        #message_display(text,x,y,color,font='freesansbold.ttf',size=30) 

        player.update()
        gameDisplay.fill(blue)

        message_display("Hehe tu nic nie ma",(display_width*0.6),(display_height*0.5),green) 
        
        
        

        
        
       

        
        count_fps()
        player.draw()
        blocky.draw()
        
        """ player.move(speedx,speedy) """
        pygame.display.update()




        
                   
        clock.tick()

menu_loop()

game_loop()



pygame.quit()
quit()