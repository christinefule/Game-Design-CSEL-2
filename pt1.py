import pygame
from pygame import mixer #class that helps to handle all kind of music inside the game.
pygame.init()

win = pygame.display.set_mode((1150,700)) #WINDOW SIZE
pygame.display.set_caption("My Sprite Game")

#VARIABLES THAT WILL IDENTIFY THE CHARACTER/SPRITE MOVEMENT
left = False
right = False
up = False
down = False

walk_counter = 0 # CHARACTER ANIMATION 

#POSITION OF THE ASSET MAIN CHARACTER
x = 510
y= 600
#DIMENTIONS
width = 40
height = 60
speed = 5
isJump = False
jumpCount = 5

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
mixer.music.load('img assets/background.wav')
mixer.music.play(-1)

def redrawWindowGame():
    global walk_counter#GET THE WALK_COUNTER
    win.blit(bg, (0,0))#TO DRAW THE BG IMAGE AT 0,0
    
    if (walk_counter + 1 >= 27):
        walk_counter = 0
        
    if left:
        win.blit(walkLeft[walk_counter//3],(x,y))#CALL WALK ARRAY        
        walk_counter += 1
    elif right:
        win.blit(walkRight[walk_counter//3],(x,y))#CALL WALK ARRAY
        walk_counter += 1  
    elif down:
        win.blit(walkDown[walk_counter//3],(x,y))#CALL WALK ARRAY
        walk_counter += 1
    elif up:
        win.blit(walkUp[walk_counter//3],(x,y))#CALL WALK ARRAY
        walk_counter += 1  
    else:
        win.blit(char, (x,y))
        walk_counter = 0
    
    pygame.display.update()#UPDATE WINDOW
    
clock = pygame.time.Clock()#INFLUENCE THE FRAME RATE WHEN CHANGING THE SPRITE IMAGE

#END OF THE OUTSIDE LOOP

#DISPLAY WINDOW
#START OF THE MAIN LOOP
run = True
while run:#RESPONSIBLE FOR THE KEYS FUNCTION AND TO DETERMINE THE FRAMERATE
    clock.tick(27)
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                                
    keys = pygame.key.get_pressed()

#KEYS FUNCTIONS CONDITION  
    if (keys[pygame.K_LEFT] and x > speed):
        x -= speed
        left = True
        right = False
        down = False
        up = False
    elif (keys[pygame.K_RIGHT] and x < 1100 - speed - width):
        x += speed
        left = False
        right = True
        down = False
        up = False
    elif (keys[pygame.K_DOWN] and y < 700 - height - speed):
        y += speed
        left = False
        right = False
        down = True
        up = False
    elif (keys[pygame.K_UP] and y > speed):
        y -= speed
        left = False
        right = False
        down = False
        up = True
    else:#IF THE CHARACTER IS NOT MOVING LEFT/RIGHT SET TO FALSE AND RESET THE ANIMATION COUNTER
        left = False
        right = False
        down = False
        up = False
        walk_counter = 0
          
#KEY JUMP CONDITION          
    if not(isJump):
        if (keys[pygame.K_SPACE]):
            isJump = True
            left = False
            right = False
            down = False
            up = False
            walk_counter =0
    else:
        if (jumpCount >= -5):
            y -= (jumpCount * abs(jumpCount)) *.5
            jumpCount -=1
        else:
            jumpCount = 5
            isJump = False  
    redrawWindowGame()#CALLOUT THE FUNCTION 
    
pygame.quit()
#END GAME
