import pygame,time,random
from Functions.simple_functions import *

pygame.init()
pygame.mixer.music.play()
pygame.mixer.music.stop()
music=True

main_character=pygame.transform.scale(main_character,(150,250))
clock=pygame.time.Clock() 
def pick_char():
    pick_char = True

    while pick_char:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all()
            gameDisplay.fill(black)
            textfont=pygame.font.Font('freesansbold.ttf',30)
            textsurf, textrect = text_objects('Pick your hero',textfont,white)
            textrect.center = ((display_width*0.5),(display_height*0.1))
            gameDisplay.blit(textsurf,textrect)
            
            rectan_button('Back',display_width*0.35,display_height*0.8,200,100,green,green_bright,menu_loop)
            rectan_button('char1',display_width*0.2,display_height*0.5,100,50,green,green_bright,set_char.char1)
            rectan_button('char2',display_width*0.4,display_height*0.5,100,50,green,green_bright,set_char.char2)
            rectan_button('char3',display_width*0.6,display_height*0.5,100,50,green,green_bright,set_char.char3)

            gameDisplay.blit(main_character,(display_width*0.4,display_height*(0.05)))
            pygame.display.update()
            clock.tick(15)

def options_loop():
    options = True
    menu = False 
    
    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all()
            gameDisplay.fill(black)
            textfont=pygame.font.Font('freesansbold.ttf',30)
            textsurf, textrect = text_objects('Project Enigma',textfont,white)
            textrect.center = ((display_width*0.5),(display_height*0.2))
            gameDisplay.blit(textsurf,textrect)

            rectan_button('Back',250,450,300,100,green,green_bright,menu_loop)
            rectan_button('X',700,50,30,30,red,red_bright,quit_all)
            rectan_button('Stop Music',250,250,200,100,green,green_bright,pause_music)
            pygame.display.update()
            clock.tick(15)
def menu_loop():
    #bez tegp się zapętla czy cos jak najpierw importuje game_loop globalnie, bo w Enigmie uzyty jest menu_loop czy cos takiego idk ;/
    from Enigma import game_loop 
    options = False
    menu = True 
    while menu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_all()
        gameDisplay.fill(black)
        textfont=pygame.font.Font('freesansbold.ttf', 60)
        textsurf, textrect = text_objects('Project Enigma',textfont,white)
        textrect.center = ((display_width*0.5),(display_height*0.5))
        gameDisplay.blit(textsurf,textrect)
       
        gameDisplay.blit(main_character,(display_width*0.4,display_height*(0.05)))

        #rectan_button(msg,x,y,w,h,ic=green,ac=green_bright,action=None,size=20,font='freesansbold.ttf')
        rectan_button('Start',250,450,250,100,green,green_bright,pick_char)
        rectan_button('X',700,50,30,30,red,red_bright,quit_all)
        rectan_button('Options',550,450,150,100,green,green_bright,options_loop)
       

        pygame.display.update()
        clock.tick(15)

menu_loop()