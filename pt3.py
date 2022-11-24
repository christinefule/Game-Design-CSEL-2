#Christine Angeline Fule
#improve player health bar make it decrement

import pygame
pygame.init()

win = pygame.display.set_mode((1150,700)) #WINDOW SIZE
pygame.display.set_caption("POKEMON HUNTER GAME")

clock = pygame.time.Clock()#INFLUENCE THE FRAME RATE WHEN CHANGING THE SPRITE IMAGE
#load the source audio/ music
hitSound = pygame.mixer.Sound('img assets/bullet.wav')
dead = pygame.mixer.Sound('img assets/deadenemy.wav')
music = pygame.mixer.music.load('img assets/themesong.wav')
pygame.mixer.music.play(-1)

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


bg = pygame.image.load('img assets/bg2.png')
char = pygame.image.load('img assets/stand.png')

#PLAYER SCORE
score = 0 
class player(object):
    def __init__(self,x,y,width,height):
    
        #VARIABLES THAT WILL IDENTIFY THE CHARACTER/SPRITE MOVEMENT
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walk_counter = 0 # CHARACTER ANIMATION 
        self.standing = True
        
        self.health = 9 #HEALTH BAR
        self.totalhealth = 9
        self.visible = True #VISIBILITY OF THE HEALTH BAR
        
        #POSITION OF THE ASSET MAIN CHARACTER
        self.x = 630
        self.y= 600
        self.hitObject = (self.x + 1, self.y + 1, 35, 53) #PLAYER HITOBJECT (rectangle) 
        
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
            
        if not(self.standing):
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
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            elif self.down:
                win.blit(walkDown[0], (self.x, self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x, self.y))
            else:
                win.blit(char, (self.x,self.y))
                self.walk_counter = 0
        self.hitObject = (self.x + 1, self.y + 1, 35, 53) #ADDED CODE FOR HITOBJECT WHICH IS THE RECTANGLE OBJECT
        #pygame.draw.rect(win, (255,0,0), self.hitObject,2) # TO DRAW THE HITOBJECT AROUND THE PLAYER
        pygame.draw.rect(win, (255,0,0),(self.hitObject[0], self.hitObject[1] -20,50,10))
        pygame.draw.rect(win, (0,128,0),(self.hitObject[0], self.hitObject[1] -20,(60 * (self.health/self.totalhealth)),10))
        
        self.hitObject = (self.x + 1, self.y + 1, 65, 38) #ADDED CODE FOR HITOBJECT WHICH IS THE RECTANGLE OBJECT
    
    def hit(self):
        self.x = 620
        self.y= 600
        if self.health > 1:
            self.health -=1
        else:
            self.health =0  
            font1 = pygame.font.SysFont('OCR A Extended', 100,True)
            text = font1.render('YOU LOSE!',1, (0,0,0))
            win.blit(text, (560 - (text.get_width()/2),200))
            pygame.display.update()
            i = 0
            while i < 200:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
       # if self.left:
       #     win.blit(walkLeft[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY        
       #     self.walk_counter += 1
       # elif self.right:
       #     win.blit(walkRight[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
       #     self.walk_counter += 1  
       # elif self.down:
       #     win.blit(walkDown[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
       #     self.walk_counter += 1
       # elif self.up:
       #     win.blit(walkUp[self.walk_counter//3],(self.x,self.y))#CALL WALK ARRAY
       #     self.walk_counter += 1  
       # else:
       #     win.blit(char, (self.x,self.y))
       #     self.walk_counter = 0
                    
#new class for handling player projectile
class projectile(object):
    #variables inside projectile class
    bullet = pygame.image.load('img assets/bullet.png')
    def  __init__(self,x,y,radius,color,facing): #constructor 1
        self.x = x
        self.y = y  
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 6* facing
        
    def draw(self,win): #constructor 2
        win.blit(self.bullet,(self.x-10,self.y-10))
        #pygame.draw.circle(win,self.color, (self.x,self.y), self.radius)
        
        
#NEW CLASS FOR ENEMY
class enemy(object):
    walkRight = [pygame.image.load('img assets/RE1.png'),pygame.image.load('img assets/RE2.png'),pygame.image.load('img assets/RE3.png'),pygame.image.load('img assets/RE4.png'),pygame.image.load('img assets/RE5.png'),
                 pygame.image.load('img assets/RE6.png'),pygame.image.load('img assets/RE7.png'),pygame.image.load('img assets/RE8.png'),pygame.image.load('img assets/RE9.png'),pygame.image.load('img assets/RE10.png'),
                 pygame.image.load('img assets/RE11.png'),pygame.image.load('img assets/RE12.png'),pygame.image.load('img assets/RE13.png'),pygame.image.load('img assets/RE14.png')]
    
    walkLeft = [pygame.image.load('img assets/LE1.png'),pygame.image.load('img assets/LE2.png'),pygame.image.load('img assets/LE3.png'),pygame.image.load('img assets/LE4.png'),pygame.image.load('img assets/LE5.png'),
                pygame.image.load('img assets/LE6.png'),pygame.image.load('img assets/LE7.png'),pygame.image.load('img assets/LE8.png'),pygame.image.load('img assets/LE9.png'),pygame.image.load('img assets/LE10.png'),
                pygame.image.load('img assets/LE11.png'),pygame.image.load('img assets/LE12.png'),pygame.image.load('img assets/LE13.png'),pygame.image.load('img assets/LE14.png')]
    
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end] #WHERE THE ENEMY STARTS AND FINISH 
        self.hitObject = (self.x + 1, self.y + 1, 68, 38) #ENEMY HIT OBJECT (rectangle) 
        self.health = 9 #HEALTH BAR
        self.visible = True #VISIBILITY OF THE enemy
        self.walk_count = 0 
        self.speed = 3

    def draw(self, win): #COMPONENTS OF THE ENEMY
        self.move()
        if self.visible:
            if self.walk_count +1 >= 33:
                self.walk_count = 0 #ANIMATION OF ENEMY. 33 BECAUSE OF THE UPPER BOUND (3 (frames) * 28 (pics)= 84)        
                
            if self.speed > 0:
                win.blit(self.walkRight[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
            else: #ENEMY GOING TO THE LEFT
                win.blit(self.walkLeft[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
                
            pygame.draw.rect(win, (255,0,0),(self.hitObject[0], self.hitObject[1] -20,50,10))
            pygame.draw.rect(win, (0,128,0),(self.hitObject[0], self.hitObject[1] -20,60 - (6 * (10 - self.health)),10))
            self.hitObject = (self.x + 1, self.y + 1, 65, 38) #ADDED CODE FOR HITOBJECT WHICH IS THE RECTANGLE OBJECT
            #pygame.draw.rect(win, (255,0,0), self.hitObject,2) # TO DRAW THE HITOBJECT AROUND THE ENEMY
        
        
    def move(self): #ATRRIBUTE OF THE ENEMY
        if self.speed > 0: #moving right
            if self.x < self.path[1] + self.speed: #IF NOT YET REACH THE FARTHEST RIGHT POINT
                self.x += self.speed
            else: #CHANGE DIRECTION AND MOVE BAKCWARD
                self.speed = self.speed * -1 
                self.x += self.speed
                self.walk_count = 0
        else: # MOVING LEFT
            if self.x > self.path[0] - self.speed: #IF NOT YET REACH THE FARTHEST LEFT POINT
                self.x += self.speed
            else:
                 self.speed = self.speed * -1
                 self.x += self.speed
                 self.walk_count = 0
               
     #METHOD TO HIT THE ENEMY
    def hit(self): #DISPLAY WHEN THE ENEMY IS HIT BY THE BULLET
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            print("CAUGHT!") 
            dead.play()   

#NEW CLASS FOR ENEMY2
class enemy2(object):
    walkRight = [pygame.image.load('img assets/ER1.png'),pygame.image.load('img assets/ER2.png'),pygame.image.load('img assets/ER3.png'),pygame.image.load('img assets/ER4.png'),pygame.image.load('img assets/ER5.png'),
                 pygame.image.load('img assets/ER6.png'),pygame.image.load('img assets/ER7.png'),pygame.image.load('img assets/ER8.png'),pygame.image.load('img assets/ER9.png'),pygame.image.load('img assets/ER10.png'),
                 pygame.image.load('img assets/ER11.png'),pygame.image.load('img assets/ER12.png'),pygame.image.load('img assets/ER13.png'),pygame.image.load('img assets/ER14.png')]
    
    walkLeft = [pygame.image.load('img assets/EL1.png'),pygame.image.load('img assets/EL2.png'),pygame.image.load('img assets/EL3.png'),pygame.image.load('img assets/EL4.png'),pygame.image.load('img assets/EL5.png'),
                pygame.image.load('img assets/EL6.png'),pygame.image.load('img assets/EL7.png'),pygame.image.load('img assets/EL8.png'),pygame.image.load('img assets/EL9.png'),pygame.image.load('img assets/EL10.png'),
                pygame.image.load('img assets/EL11.png'),pygame.image.load('img assets/EL12.png'),pygame.image.load('img assets/EL13.png'),pygame.image.load('img assets/LE14.png')]
    
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end] #WHERE THE ENEMY STARTS AND FINISH 
        self.hitObject2 = (self.x + 1, self.y + 1, 52, 48) #ENEMY HIT OBJECT (rectangle) 
        self.health = 9
        self.totalhealth =9
        self.visible = True
        
        self.walk_count = 0 
        self.speed = 3

    def draw(self, win): #COMPONENTS OF THE ENEMY
        self.move()
        if self.visible:
            if self.walk_count +1 >= 33:
                self.walk_count = 0 #ANIMATION OF ENEMY. 33 BECAUSE OF THE UPPER BOUND (3 (frames) * 28 (pics)= 84)        
                
            if self.speed > 0:
                win.blit(self.walkRight[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
            else: #ENEMY GOING TO THE LEFT
                win.blit(self.walkLeft[self.walk_count//3],(self.x,self.y))
            pygame.draw.rect(win, (255,0,0),(self.hitObject2[0], self.hitObject2[1] -20,50,10))
            pygame.draw.rect(win, (0,128,0),(self.hitObject2[0], self.hitObject2[1] -20,(60 * (self.health/self.totalhealth)),10))
            self.hitObject2 = (self.x + 1, self.y + 1, 52, 48) #ADDED CODE FOR HITOBJECT WHICH IS THE RECTANGLE OBJECT
            #pygame.draw.rect(win, (0,0,0), self.hitObject2,2) # TO DRAW THE HITOBJECT AROUND THE ENEMY
            
        
    def move(self): #ATRRIBUTE OF THE ENEMY
        if self.speed > 0: #moving right
            if self.x < self.path[1] + self.speed: #IF NOT YET REACH THE FARTHEST RIGHT POINT
                self.x += self.speed
            else: #CHANGE DIRECTION AND MOVE BAKCWARD
                self.speed = self.speed * -1 
                self.x += self.speed
                self.walk_count = 0
        else: # MOVING LEFT
            if self.x > self.path[0] - self.speed: #IF NOT YET REACH THE FARTHEST LEFT POINT
                self.x += self.speed
            else:
                 self.speed = self.speed * -1
                 self.x += self.speed
                 self.walk_count = 0
                 
     #METHOD TO HIT THE ENEMY
    def hit(self): #DISPLAY WHEN THE ENEMY IS HIT BY THE BULLET
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            print("CAUGHT!")   
            dead.play()           
    
#NEW CLASS FOR ENEMY3
class enemy3(object):
    walkDown = [pygame.image.load('img assets/DE1.png'),pygame.image.load('img assets/DE2.png'),pygame.image.load('img assets/DE3.png'),pygame.image.load('img assets/DE4.png'),pygame.image.load('img assets/DE5.png'),
                 pygame.image.load('img assets/DE6.png'),pygame.image.load('img assets/DE7.png'),pygame.image.load('img assets/DE8.png'),pygame.image.load('img assets/DE9.png'),pygame.image.load('img assets/DE10.png'),
                 pygame.image.load('img assets/DE11.png'),pygame.image.load('img assets/DE12.png'),pygame.image.load('img assets/DE13.png'),pygame.image.load('img assets/DE14.png')]
    
    walkUp = [pygame.image.load('img assets/UE1.png'),pygame.image.load('img assets/UE2.png'),pygame.image.load('img assets/UE3.png'),pygame.image.load('img assets/UE4.png'),pygame.image.load('img assets/UE5.png'),
                pygame.image.load('img assets/UE6.png'),pygame.image.load('img assets/UE7.png'),pygame.image.load('img assets/UE8.png'),pygame.image.load('img assets/UE9.png'),pygame.image.load('img assets/UE10.png'),
                pygame.image.load('img assets/UE11.png'),pygame.image.load('img assets/UE12.png'),pygame.image.load('img assets/UE13.png'),pygame.image.load('img assets/UE14.png')]
    
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end] #WHERE THE ENEMY STARTS AND FINISH 
        self.hitObject3 = (self.x + 1, self.y + 1, 35, 53) #ENEMY HIT OBJECT (rectangle) 
        self.health = 9
        self.visible = True
        
        self.walk_count = 0 
        self.speed = 3

    def draw(self, win): #COMPONENTS OF THE ENEMY
        self.move()
        if self.visible:
            if self.walk_count +1 >= 33:
                self.walk_count = 0 #ANIMATION OF ENEMY. 33 BECAUSE OF THE UPPER BOUND (3 (frames) * 28 (pics)= 84)        
                
            if self.speed > 0:
                win.blit(self.walkDown[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
            else: #ENEMY GOING TO THE LEFT
                win.blit(self.walkUp[self.walk_count//3],(self.x,self.y))
            pygame.draw.rect(win, (255,0,0),(self.hitObject3[0], self.hitObject3[1] -20,50,10))
            pygame.draw.rect(win, (0,128,0),(self.hitObject3[0], self.hitObject3[1] -20,60 - (6 * (10 - self.health)),10))
            self.hitObject3 = (self.x + 1, self.y + 1, 32, 30) #ADDED CODE FOR HITOBJECT WHICH IS THE RECTANGLE OBJECT
            #pygame.draw.rect(win, (0,0,0), self.hitObject3,2) # TO DRAW THE HITOBJECT AROUND THE ENEMY
            
        
    def move(self): #ATRRIBUTE OF THE ENEMY
        if self.speed > 0: #moving right
            if self.x < self.path[1] + self.speed: #IF NOT YET REACH THE FARTHEST RIGHT POINT
                self.x += self.speed
            else: #CHANGE DIRECTION AND MOVE BAKCWARD
                self.speed = self.speed * -1 
                self.x += self.speed
                self.walk_count = 0
        else: # MOVING LEFT
            if self.x > self.path[0] - self.speed: #IF NOT YET REACH THE FARTHEST LEFT POINT
                self.x += self.speed
            else:
                 self.speed = self.speed * -1
                 self.x += self.speed
                 self.walk_count = 0
                 
    #METHOD TO HIT THE ENEMY
    def hit(self): #DISPLAY WHEN THE ENEMY IS HIT BY THE BULLET
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            print("CAUGHT!")  
            dead.play()          
            
                
def redrawWindowGame():
    win.blit(bg, (0,0))#TO DRAW THE BG IMAGE AT 0,0
    text = font.render('Score: ' + str(score), 1, (255,255,0)) #RENDERING SOME TEXT AND DISPLAY ON SCREEN
    win.blit(text, (970,30))#SCORE POSITION
    
    #global walk_counter#GET THE WALK_COUNTER
    play.draw(win)
    monster.draw(win)
    monster2.draw(win)
    monster3.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()#UPDATE WINDOW
clock = pygame.time.Clock()
#YOU CAN CHANGE THE COLOR HERE OF THE WIN 
def drawWinGame():
    win.blit(bg, (0,0))
    play.draw(win)
    font1 = pygame.font.SysFont('OCR A Extended', 100,True)
    text = font1.render('YOU WIN!',1, (0,0,0))
    win.blit(text, (560 - (text.get_width()/2),200))
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
#END OF THE OUTSIDE LOOP

#main loop
#DISPLAY WINDOW
#START OF THE MAIN LOOP
play = player(200,410,100,100)#NSTANCE OF THE MAIN PLAYER
monster = enemy (230,230,100,100,400) #INSTANCE OF THE ENEMY
monster2 = enemy2 (600,340,200,200,700)#INSTANCE OF THE ENEMY
monster3 = enemy3 (200,520,200,200,300)#INSTANCE OF THE ENEMY
bullets = []
shootLoop = 0
run = True

#MAIN LOOP
font = pygame.font.SysFont('Orbitron', 30, True,True)#TEXT FONT, SIZE, BOLD, ITALIC  

while run:#RESPONSIBLE FOR THE KEYS FUNCTION AND TO DETERMINE THE FRAMERATE
    clock.tick(27)         
    #NO. OF BULLET RELEASE
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
     #add the projectile class in main loop = player with gun
    for bullet in bullets:
        if monster.visible:
            #TO CHECK X COORDINATE
            if bullet.y - bullet.radius < monster.hitObject[1] + monster.hitObject[3] and bullet.y + bullet.radius > monster.hitObject[1]:
            #TO CHECK Y COORDINATE
                if bullet.x + bullet.radius > monster.hitObject[0] and bullet.x - bullet.radius < monster.hitObject[0] + monster.hitObject[2]:
                    monster.hit()#HIT FUNCTION CALL
                    score += 1 #SCORING
                    bullets.pop(bullets.index(bullet))#TO USE BULLET LIST
        if monster2.visible:
            if bullet.y - bullet.radius < monster2.hitObject2[1] + monster2.hitObject2[3] and bullet.y + bullet.radius > monster2.hitObject2[1]:
            #TO CHECK Y COORDINATE
                if bullet.x + bullet.radius > monster2.hitObject2[0] and bullet.x - bullet.radius < monster2.hitObject2[0] + monster2.hitObject2[2]:
                    monster2.hit()#HIT FUNCTION CALL
                    score += 1 #SCORING 
                    bullets.pop(bullets.index(bullet))#TO USE BULLET LIST    
        if monster3.visible:
            #TO CHECK X COORDINATE
            if bullet.y - bullet.radius < monster3.hitObject3[1] + monster3.hitObject3[3] and bullet.y + bullet.radius > monster3.hitObject3[1]:
            #TO CHECK Y COORDINATE
                if bullet.x + bullet.radius > monster3.hitObject3[0] and bullet.x - bullet.radius < monster3.hitObject3[0] + monster3.hitObject3[2]:
                    monster3.hit()#HIT FUNCTION CALL
                    score += 1 #SCORING
                    bullets.pop(bullets.index(bullet))#TO USE BULLET LIST    
        #checks if the bullet is still in the screen
        if   bullet.x < 1100 and bullet.x > 0:
            bullet.x += bullet.speed 
        else:
            bullets.pop(bullets.index(bullet))
                                
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and shootLoop == 0:
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
            shootLoop = 1 #NEWLY ADDED
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
    
    #CHECKS IF THE PLAYER COLLIDED WITH THE ENEMY
    if(play.hitObject[0]>=monster.hitObject[0] and play.hitObject[0]<=monster.hitObject[0]+monster.hitObject[2]):#checks if the box's left is in monster border 
        if(play.hitObject[1]>=monster.hitObject[1] and play.hitObject[1]<=monster.hitObject[1]+monster.hitObject[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster.hitObject[1] and play.hitObject[1]+play.hitObject[3]<=monster.hitObject[1]+monster.hitObject[3]):
            play.hit()
    elif(play.hitObject[0]+play.hitObject[2]>=monster.hitObject[0] and play.hitObject[0]+play.hitObject[2]<=monster.hitObject[0]+monster.hitObject[2]):
        if(play.hitObject[1]>=monster.hitObject[1] and play.hitObject[1]<=monster.hitObject[1]+monster.hitObject[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster.hitObject[1] and play.hitObject[1]+play.hitObject[3]<=monster.hitObject[1]+monster.hitObject[3]):
            play.hit()

    if(play.hitObject[0]>=monster2.hitObject2[0] and play.hitObject[0]<=monster2.hitObject2[0]+monster2.hitObject2[2]):#checks if the box's left is in monster2 border 
        if(play.hitObject[1]>=monster2.hitObject2[1] and play.hitObject[1]<=monster2.hitObject2[1]+monster2.hitObject2[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster2.hitObject2[1] and play.hitObject[1]+play.hitObject[3]<=monster2.hitObject2[1]+monster2.hitObject2[3]):
            play.hit()
    elif(play.hitObject[0]+play.hitObject[2]>=monster2.hitObject2[0] and play.hitObject[0]+play.hitObject[2]<=monster2.hitObject2[0]+monster2.hitObject2[2]):
        if(play.hitObject[1]>=monster2.hitObject2[1] and play.hitObject[1]<=monster2.hitObject2[1]+monster2.hitObject2[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster2.hitObject2[1] and play.hitObject[1]+play.hitObject[3]<=monster2.hitObject2[1]+monster2.hitObject2[3]):
            play.hit()

    if(play.hitObject[0]>=monster3.hitObject3[0] and play.hitObject[0]<=monster3.hitObject3[0]+monster3.hitObject3[2]):#checks if the box's left is in monster3 border 
        if(play.hitObject[1]>=monster3.hitObject3[1] and play.hitObject[1]<=monster3.hitObject3[1]+monster3.hitObject3[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster3.hitObject3[1] and play.hitObject[1]+play.hitObject[3]<=monster3.hitObject3[1]+monster3.hitObject3[3]):
            play.hit()
    elif(play.hitObject[0]+play.hitObject[2]>=monster3.hitObject3[0] and play.hitObject[0]+play.hitObject[2]<=monster3.hitObject3[0]+monster3.hitObject3[2]):
        if(play.hitObject[1]>=monster3.hitObject3[1] and play.hitObject[1]<=monster3.hitObject3[1]+monster3.hitObject3[3]):
            play.hit()
        elif(play.hitObject[1]+play.hitObject[3]>=monster3.hitObject3[1] and play.hitObject[1]+play.hitObject[3]<=monster3.hitObject3[1]+monster3.hitObject3[3]):
            play.hit()
            

    if score >= 30:
        drawWinGame()
    else:
        redrawWindowGame()#CALLOUT THE FUNCTION 
    
pygame.quit()
#END GAME
