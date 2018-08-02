import pygame,time,random


from Functions.simple_functions import *
main_char=pygame.transform.scale(main_char,(150,250))
clock=pygame.time.Clock() 

def menu_loop():
    from Enigma import game_loop as gl
    from Functions.simple_functions import quit_all 
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
       
        gameDisplay.blit(main_char,(display_width*0.4,display_height*(0.05)))
        
        rectan_button('Start',250,450,300,100,green,green_bright,gl)
        rectan_button('X',700,50,30,30,red,red_bright,quit_all)
        
       

        pygame.display.update()
        clock.tick(15)

menu_loop()