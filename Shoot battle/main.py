#Importing all the modules
try:
    import time, random, sys, os
except ImportError:
    print("Make sure to have the time module")
    sys.exit()
try:
    import pygame
except ImportError:
    print("Make sure you have python 3 and pygame.")
    sys.exit()
try:
    import MainMenu
except Exception:
    print("Make sure to have the extra files")
from pygame import freetype


#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 1300, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Name")
font_50 = pygame.freetype.Font("Font.ttf", 50)
score = [0,0]


class Player():
    def __init__(self,x,y, Num, Color, mode):
        #Defining a bunch of basic variables
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        #Making the hitbox
        self.image = pygame.Surface(([self.width,self.height]))
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width
        #Other miscellanious variables
        self.num = Num
        self.color = Color
        self.x_change = 0
        self.y_change = 0
        self.bNum = Num * 10 - 10
        self.shoot = False
        self.dead = False
        self.mode = mode
        #Used for bots
        self.ShootCooldown = 5

    def draw(self):
        pygame.draw.rect(gameDisplay,self.color,(self.x, self.y, self.width, self.height),0)

    def KeyPress(self, player):
        key = pygame.key.get_pressed()

        if self.num == 1:
            if key[ord('a')]:
                self.x_change = -5
            if key[ord('d')]:
                self.x_change = 5
            if key[ord('w')]:
                self.y_change = -5
            if key[ord('s')]:
                self.y_change = 5

            if key[ord('a')] == 0 and self.x_change == -5:
                self.x_change = 0
            if key[ord('d')] == 0 and self.x_change == 5:
                self.x_change = 0
            if key[ord('w')] == 0 and self.y_change == -5:
                self.y_change = 0
            if key[ord('s')] == 0 and self.y_change == 5:
                self.y_change = 0
                

            if self.x_change == -5 and self.x >= 0:
                self.x += self.x_change
            if self.x_change == 5 and self.x <= 495 - self.width:
                self.x += self.x_change
            if self.y_change == -5 and self.y >= -50:
                self.y += self.y_change
            if self.y_change == 5 and self.y <= 800:
                self.y += self.y_change



        if self.num == 2 and self.mode == "2p":
            if key[pygame.K_LEFT]:
                self.x_change = -5
            if key[pygame.K_RIGHT]:
                self.x_change = 5
            if key[pygame.K_UP]:
                self.y_change = -5
            if key[pygame.K_DOWN]:
                self.y_change = 5

            if key[pygame.K_LEFT] == 0 and self.x_change == -5:
                self.x_change = 0
            if key[pygame.K_RIGHT] == 0 and self.x_change == 5:
                self.x_change = 0
            if key[pygame.K_UP] == 0 and self.y_change == -5:
                self.y_change = 0
            if key[pygame.K_DOWN] == 0 and self.y_change == 5:
                self.y_change = 0

            if self.x_change == -5 and self.x >= 500:
                self.x += self.x_change
            if self.x_change == 5 and self.x <= 945:
                self.x += self.x_change
            if self.y_change == -5 and self.y >= -50:
                self.y += self.y_change
            if self.y_change == 5 and self.y <= 800:
                self.y += self.y_change

        if self.mode == "AI" and self.num == 2:
            if abs(self.y - player.y) <= 300:
                if self.y >= player.y:
                    self.y_change = -1 * random.randint(3,7)
                if self.y <= player.y:
                    self.y_change = random.randint(3,7)
            else:
                if self.y >= player.y:
                    self.y_change = random.randint(3,7)
                if self.y <= player.y:
                    self.y_change = -1 * random.randint(3,7)
            if player.y - 200 <= self.y <= player.y + 200 and self.ShootCooldown <= 0:
                self.shoot = True
                self.ShootCooldown = 10
                self.y_change = random.randint(-25,25)
            else:
                self.ShootCooldown -= 1

            self.y += self.y_change
        
            


    def update(self, Bullets, Player):
        if self.dead == False:
            self.draw()
            self.KeyPress(Player)
            self.rect.top = self.y
            self.rect.bottom = self.y + self.height
            self.rect.left = self.x
            self.rect.right = self.x + self.width
            for bullet in Bullets:
                if pygame.sprite.collide_rect(self, bullet) == True:
                    if self.num == 1:
                        score[1] += 1
                    else:
                        score[0] += 1
                    self.dead = True
            if self.y >= 800:
                self.y = -49
            if self.y <= -50:
                self.y = 799

                    
                    
class Bullet():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 15
        self.image = pygame.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width
        self.color = (200,200,0)
        self.direction = "none"

    def draw(self):
        pygame.draw.rect(gameDisplay,self.color,(self.x, self.y, self.width, self.height),0)

    def movement(self):
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10
            

    def reset(self,x,y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        

    def update(self):
        if -40 <= self.x <= 979:
            self.draw()
            self.movement()
        else:
            if self.direction == "left":
                self.x = 970
            if self.direction == "right":
                self.x = -30
        self.rect.top = self.y
        self.rect.bottom = self.y + self.height
        self.rect.left = self.x
        self.rect.right = self.x + self.width

def game_loop(mode):
    game_run = True

    Players = [Player(100,100,1,(150,0,0), mode),Player(700,650,2,(0,0,150), mode)]
    Bullets = []
    for i in range(20):
        Bullets.append(Bullet(-100,-100))

    while game_run == True:

        #Drawing the background
        pygame.draw.rect(gameDisplay,(225,0,0),(0,0,500,800),0)
        pygame.draw.rect(gameDisplay,(0,0,225),(500,0,500,800),0)
        pygame.draw.rect(gameDisplay,(150,0,0),(1000,0,300,800),0)

        #Displaying the score
        text_surface, rect = font_50.render(("Red: " + str(score[0])), (0, 0, 0))
        gameDisplay.blit(text_surface, (1050, 200))
        text_surface, rect = font_50.render(("Blue: " + str(score[1])), (0, 0, 0))
        gameDisplay.blit(text_surface, (1050, 500))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Players[0].shoot = True
                if mode == "2p":
                    if event.key == pygame.K_RALT:
                        Players[1].shoot = True
                    

        for i, player in enumerate(Players):
            player.update(Bullets, Players[0])
            if player.shoot == True:
                if i == 0:
                    Bullets[player.bNum].reset(player.x+50,player.y+10,"right")
                    player.bNum += 1
                    if player.bNum == 9:
                        player.bNum = 0
                else:
                    Bullets[player.bNum].reset(player.x-30,player.y+10,"left")
                    player.bNum += 1
                    if player.bNum == 19:
                        player.bNum = 10
                player.shoot = False
            if player.dead == True:
                game_loop(mode)


        for bullet in Bullets:
            bullet.update()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    MainMenu.mainMenu()
