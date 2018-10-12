import pygame,time,random,sys #tam wszystko co sie moze przydac  #sys,os,math moze potem






pygame.init()
#Rozmiar Okna Gry do okreslania rozmiaru okna gry oraz polozenia buttonow itp czasem przydatne
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.mixer.music.load('./Functions/sounds/pirate.wav')

char_img0=pygame.image.load('./Functions/textures/main_char/main_front0.png')
char_img1=pygame.image.load('./Functions/textures/main_char/main_front1.png')
char_img2=pygame.image.load('./Functions/textures/main_char/main_front2.png')

#Colory
black = (0,0,0)
white = (255,255,255)
red = (150,0,0) 
red_bright = (255,0,0) 
blue = (0,0,255)  
green = (0,150,0)
green_bright = (0 ,255, 0) 
brown = (218,165,32) 

x=400
y=400


x_change=0
y_change=0

cSec=0
cFrame=0
FPS=0

def count_fps():
    global cSec,cFrame,FPS
    if cSec == time.strftime("%S"):
        cFrame+=1
        
    else:
        FPS = cFrame
        cFrame = 0
        cSec=time.strftime("%S")
    message_display(str(FPS),(display_width*0.2),(display_height*0.1),green)
    

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
def rectan_button(msg,x,y,w=100,h=100,ic=green,ac=green_bright,action=None,size=20,font='freesansbold.ttf'): 
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

#Game funkcje

""" 
def main_char_pos_draw(main_character=char_img0,x=0.5*display_width,y=0.5*display_height):
    gameDisplay.blit(main_character,(x,y)) """



            





class Platform(object):
    def __init__(self,x,y,w,h,ic):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic=black
        Platform.h=h
        Platform.y=y
        Platform.x=x
        Platform.w=w
    
    def draw(self):
        pygame.draw.rect(gameDisplay,self.ic,(self.x,self.y,self.w,self.h))
    


class Player(Platform):
    def __init__(self,x,y,main_character):
        self.x = x
        self.y = y
        self.main_character = main_character
        self.jump=False
        self.event=None
        self.direction=[0,0]
        self.speed=6
        self.gravity=3
        self.m=2
        self.v=7

    def draw(self):
        gameDisplay.blit(self.main_character,(self.x,self.y))
    def update(self):
        self.x += self.speed*self.direction[1]
        print (self.jump)
        #self.y += self.speed*self.direction[0]  chodzenie po mapie na przyklad
        self.y+=self.gravity
        if self.x > display_width - 40:
            self.x=display_width -40
        if self.x< 0:
            self.x=0
        if self.y>display_height-50:
            self.jump=False
            self.y=display_height-50
            self.v = 7
            self.gravity=0
 
        if self.jump:
            if self.v>0:
                F= (0.5*self.m*(self.v*self.v))
            else:
                F=  -(0.5*self.m*(self.v*self.v))
            self.y= self.y - F
            self.v= self.v -0.5
        a=((self.y-40 > Platform.y  and self.y-40 < Platform.y+35) and  (self.x > Platform.x-30 and self.x < Platform.x + Platform.w))
        if  a :

            #self.y-40 > Platform.y and 
            self.y=Platform.y-40
            self.v=7
            self.jump=False
            self.gravity=0
        else: 
            gravity=3    
    def move(self,event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.jump=True
                #self.direction[0]-=1
            """ elif event.key == pygame.K_DOWN:
                self.direction[0]+=1 """
            if event.key == pygame.K_RIGHT:
                self.direction[1]+=1 
            elif event.key == pygame.K_LEFT:
                self.direction[1]-=1
                
        if event.type == pygame.KEYUP:
            #if event.key == pygame.K_UP:
               # self.direction[0]+=1
            """ elif event.key == pygame.K_DOWN:
                self.direction[0]-=1  """
            if event.key == pygame.K_RIGHT:
                self.direction[1]-=1
            elif event.key == pygame.K_LEFT:
                self.direction[1]+=1         
        
            
