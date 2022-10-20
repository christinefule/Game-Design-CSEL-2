#Optimizing the coe to OOP and adding class projectile --> sword
from re import X
import pygame
from pygame import mixer #class that helps to handle all kind of music inside the game.
pygame.init()

win = pygame.display.set_mode((1150,700)) #WINDOW SIZE
pygame.display.set_caption("My Sprite Game")

clock = pygame.time.Clock()#INFLUENCE THE FRAME RATE WHEN CHANGING THE SPRITE IMAGE

#OUTSIDE THE LOOP
#source image/sprite 
#PYGAME TO LOAD THE IMAGE SPRITES
walkRight = [pygame.image.load('img assets/R1.png'),pygame.image.load('img assets/R2.png'),pygame.image.load('img assets/R3.png'),pygame.image.load('img assets/R4.png'),pygame.image.load('img assets/R5.png'),pygame.image.load('img assets/R6.png'),pygame.image.load('img assets/R7.png'),
             pygame.image.load('img assets/R8.png'),pygame.image.load('img assets/R9.png'),pygame.image.load('img assets/R10.png'),pygame.image.load('img assets/R11.png'),pygame.image.load('img assets/R12.png'),pygame.image.load('img assets/R13.png'),pygame.image.load('img assets/R14.png'),
             pygame.image.load('img assets/R15.png'),pygame.image.load('img assets/R16.png'),pygame.image.load('img assets/R17.png'),pygame.image.load('img assets/R18.png'),pygame.image.load('img assets/R19.png'),pygame.image.load('img assets/R20.png'),pygame.image.load('img assets/R21.png')]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
walkLeft = [pygame.image.load('img assets/L1.png'),pygame.image.load('img assets/L2.png'),pygame.image.load('img assets/L3.png'),pygame.image.load('img assets/L4.png'),pygame.image.load('img assets/L5.png'),pygame.image.load('img assets/L6.png'),pygame.image.load('img assets/L7.png'),
            pygame.image.load('img assets/L8.png'),pygame.image.load('img assets/L9.png'),pygame.image.load('img assets/L10.png'),pygame.image.load('img assets/L11.png'),pygame.image.load('img assets/L12.png'),pygame.image.load('img assets/L13.png'),pygame.image.load('img assets/L14.png'),
            pygame.image.load('img assets/L15.png'),pygame.image.load('img assets/L16.png'),pygame.image.load('img assets/L17.png'),pygame.image.load('img assets/L18.png'),pygame.image.load('img assets/L19.png'),pygame.image.load('img assets/L20.png'),pygame.image.load('img assets/L21.png')]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
walkDown = [pygame.image.load('img assets/D1.png'),pygame.image.load('img assets/D2.png'),pygame.image.load('img assets/D3.png'),pygame.image.load('img assets/D4.png'),pygame.image.load('img assets/D5.png'),pygame.image.load('img assets/D6.png'),pygame.image.load('img assets/D7.png'),
             pygame.image.load('img assets/D8.png'),pygame.image.load('img assets/D9.png'),pygame.image.load('img assets/D10.png'),pygame.image.load('img assets/D11.png'),pygame.image.load('img assets/D12.png'),pygame.image.load('img assets/D13.png'),pygame.image.load('img assets/D14.png'),
             pygame.image.load('img assets/D15.png'),pygame.image.load('img assets/D16.png'),pygame.image.load('img assets/D17.png'),pygame.image.load('img assets/D18.png'),pygame.image.load('img assets/D19.png'),pygame.image.load('img assets/D20.png'),pygame.image.load('img assets/D21.png')]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
walkUp = [pygame.image.load('img assets/U1.png'),pygame.image.load('img assets/U2.png'),pygame.image.load('img assets/U3.png'),pygame.image.load('img assets/U4.png'),pygame.image.load('img assets/U5.png'),pygame.image.load('img assets/U6.png'),pygame.image.load('img assets/U7.png'),
             pygame.image.load('img assets/U8.png'),pygame.image.load('img assets/U9.png'),pygame.image.load('img assets/U10.png'),pygame.image.load('img assets/U11.png'),pygame.image.load('img assets/U12.png'),pygame.image.load('img assets/U13.png'),pygame.image.load('img assets/U14.png'),
             pygame.image.load('img assets/U15.png'),pygame.image.load('img assets/U16.png'),pygame.image.load('img assets/U17.png'),pygame.image.load('img assets/U18.png'),pygame.image.load('img assets/U19.png'),pygame.image.load('img assets/U20.png'),pygame.image.load('img assets/U21.png')]


bg = pygame.image.load('img assets/bg.png')
char = pygame.image.load('img assets/stand.png')
mixer.music.load('img assets/themesong.wav')
mixer.music.play(-1)

class player(object):
    def __init__(self,x,y,width,height):
    
        #VARIABLES THAT WILL IDENTIFY THE CHARACTER/SPRITE MOVEMENT
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_counter = 0 # CHARACTER ANIMATION 
        self.standing = True

        #POSITION OF THE ASSET MAIN CHARACTER
        self.x = 510
        self.y= 600
        #DIMENTIONS
        self.width = 40
        self.height = 60
        self.speed = 5
        self.isJump = False
        self.jumpCount = 5
        
#function that will enable us to use the key
#construction for the class player
    def draw(self,win): 
        if (self.walk_counter + 1 >= 27):
            self.walk_counter = 0
            
        if self.left:
            win.blit(walkLeft[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY        
            self.walk_counter += 1
        elif self.right:
            win.blit(walkRight[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
            self.walk_counter += 1  
        elif self.down:
            win.blit(walkDown[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
            self.walk_counter += 1
        elif self.up:
            win.blit(walkUp[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
            self.walk_counter += 1  
        else:
            win.blit(char, (self.x,self.y))
            self.walk_counter = 0

#new class for handling player projectile
class projectile(object):
    #variables inside projectile class
    def  __init__(self,x,y,radius,color,facing): #constructor 1
        self.x = x
        self.y = y  
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 7* facing
        
    def draw(self,win): #constructor 2
        pygame.draw.circle(win,self.color, (self.x,self.y), self.radius)
        
def redrawWindowGame():
    win.blit(bg, (0,0))#TO DRAW THE BG IMAGE AT 0,0
    #global walk_counter#GET THE WALK_COUNTER
    play.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()#UPDATE WINDOW

#END OF THE OUTSIDE LOOP

#main loop
#DISPLAY WINDOW
#START OF THE MAIN LOOP
play = player(200,410,100,100)#instance of player class
bullets = []
run = True
while run:#RESPONSIBLE FOR THE KEYS FUNCTION AND TO DETERMINE THE FRAMERATE
    clock.tick(27)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
     #add the projectile class in main loop = player with gun
    for bullet in bullets:
        if bullet.x < 1100 and bullet.x > 0:
             bullet.x += bullet.speed 
        else:
            bullets.pop(bullets.index(bullet))
                                
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if play.left:
            facing = -3
        elif play.up:
            facing = 3
        elif play.down:
            facing = -3
        else:
            facing = 3
        if len(bullets) < 1:
            bullets.append(projectile(round(play.x + play.width //2), round(play.y + play.height //2), 10,(255,0,0), facing ))

#KEYS FUNCTIONS CONDITION  
    if (keys[pygame.K_LEFT] and  play.x > play.speed):
         play.x -=  play.speed
         play.left = True
         play.right = False
         play.down = False
         play.up = False
         play.standing = False #added object in the class
         
    elif (keys[pygame.K_RIGHT] and  play.x < 1100 -  play.speed -  play.width):
         play.x +=  play.speed
         play.left = False
         play.right = True
         play.down = False
         play.up = False
         play.standing = False #added object in the class
    elif (keys[pygame.K_DOWN] and  play.y < 700 -  play.height -  play.speed):
         play.y +=  play.speed
         play.left = False
         play.right = False
         play.down = True
         play.up = False
         play.standing = False #added object in the class
    elif (keys[pygame.K_UP] and  play.y >  play.speed):
         play.y -=  play.speed
         play.left = False
         play.right = False
         play.down = False
         play.up = True
         play.standing = False #added object in the class
    else:#IF THE CHARACTER IS NOT MOVING LEFT/RIGHT SET TO FALSE AND RESET THE ANIMATION COUNTER
         #play.left = False
         #play.right = False
         #play.down = False
        # play.up = False
         play.standing = True #the character will side view whether left or right
         play.walk_counter = 0
          
#KEY JUMP CONDITION          
    if not( play.isJump):
        if (keys[pygame.K_SPACE]):
             play.isJump = True
             play.left = False
             play.right = False
             play.down = False
             play.up = False
             play.walk_counter = 0
    else:
        if ( play.jumpCount >= -5):
            neg = 1
            if play.jumpCount < 0:
                neg = -1
            #play.y -= ( play.jumpCount * abs( play.jumpCount)) *.5
            play.y -=(play.jumpCount ** 2) * 0.5 * neg
            play.jumpCount -=1
        else:
             play.jumpCount = 5
             play.isJump = False  
    redrawWindowGame()#CALLOUT THE FUNCTION 
    
pygame.quit()
#END GAME
