import pygame,time,random #tam wszystko co sie moze przydac  #sys,os,math moze potem

pygame.init()
#Rozmiar Okna Gry do okreslania rozmiaru okna gry oraz polozenia buttonow itp czasem przydatne
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load('.\Functions\sounds\pirate.wav')

main_char=pygame.image.load('.\Functions\\textures\\main_char\\main_front0.png')
#Colory
black = (0,0,0)
white = (255,255,255)
red = (150,0,0) 
red_bright = (255,0,0) 
blue = (0,0,255)  
green = (0,150,0)
green_bright = (0 ,255, 0) 
brown = (218,165,32) 

def pause_music():
    """pauzuje muzyke, uzywa Menu.music"""
    from Functions import Menu
    if Menu.music == False:
        pygame.mixer.music.unpause()
        Menu.music = True
    else:
        pygame.mixer.music.pause()
        Menu.music = False
def quit_all():
    """wylacza pygame i pythona, przydatne gdy chcemy wyslac do przycisku EXIT jedną akcje, a potrzebujemy wykonac te obie.
    w środku 'pygame.quit' oraz 'quit'"""
    pygame.quit
    quit()

def text_objects(text,font,color):
    textsurface = font.render(text,True, color, None)    
    return textsurface, textsurface.get_rect()  
def rectan_button(msg,x,y,w,h,ic=green,ac=green_bright,action=None,size=20,font='freesansbold.ttf'): 
    """Funckja bierze wiadomosc (msg - string) na przycisku , wymiary startowe lewego gornego rogu przycisku (x i y)
    szerokosc i dlugosc (w i h), color nieaktywny(ic=inactive color) i aktywny(po najechaniu(ac)) oraz akcje(action - jakas funkcja) ktora ma sie wykonac)
    mozna wybrac czcionke i jej wielkosc """
    mouse = pygame.mouse.get_pos() #pobiera pozycje myszki i zwraca x w mouse[0] i y w mouse[1]
    click = pygame.mouse.get_pressed() # click[0] lewy, click[1] srodkowy , click[2] prawy przycisk myszy 
    
        #print(mouse)
    a = (x+w > mouse[0] and x < mouse[0] and y+h>mouse[1] and y < mouse[1]) #warunek na to , czy pozycja myszki jest w prostokacie przycisku
    if a: 
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))  #rysuje  jasniejszy prostokąt, wydaje sie ze podswietlony, gdy myszka na nim.
        
        if click[0]==1 and action!=None:
            #sleep zeby sie nie wcisnely 2 przyciski jak np. wychodzisz z opcji, a w miejscu przycisku 'back' w glownym menu jest 'start'
            time.sleep(0.1)
            action() 
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h)) #rysuje  ciemny prostokat, jesli a nie jest prawdą
        

    # tutaj tworzy sie napis na srodku ekranu. 
    # mozna dorzucic opcje wyboru 
    textfont = pygame.font.Font('freesansbold.ttf',20)
    textsurf,textrect = text_objects(msg,textfont,black)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textsurf,textrect)

def message_display(text,x,y,color,font='freesansbold.ttf',size=30):
    "Wyświetla napis na ekranie np. game over itp."
    textfont=pygame.font.Font(font,size)
    textsurf, textrect = text_objects(text,textfont,color)
    textrect.center = ((x),(y))
    gameDisplay.blit(textsurf,textrect)