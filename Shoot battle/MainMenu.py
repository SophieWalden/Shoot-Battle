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
    import main
except ImportError:
    print("Make sure you have the extra files")
from pygame import freetype


#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 1300, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Name")
font_150 = pygame.freetype.Font("BoldFont.ttf", 150)
font_35 = pygame.freetype.Font("Font.ttf", 35)

def mainMenu():
    game_run = True

    while game_run == True:

        gameDisplay.fill((100,100,100))
        pos = pygame.mouse.get_pos()
        
        text_surface, rect = font_150.render(("Shoot Battle"), (0, 0, 0))
        gameDisplay.blit(text_surface, (300, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 600 and pos[1] <= 700:
                    main.game_loop("2p")
                if pos[0] >= 900 and pos[0] <= 1100 and pos[1] >= 600 and pos[1] <= 700:
                    main.game_loop("AI")

        if pos[0] >= 200 and pos[0] <= 400 and pos[1] >= 600 and pos[1] <= 700:
            pygame.draw.rect(gameDisplay,(150,0,0),(200,600,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(250,0,0),(200,600,200,100),0)
        pygame.draw.rect(gameDisplay,(100,0,0),(200,600,200,100),5)
        text_surface, rect = font_35.render(("2 Players"), (0, 0, 0))
        gameDisplay.blit(text_surface, (230, 630))

        if pos[0] >= 900 and pos[0] <= 1100 and pos[1] >= 600 and pos[1] <= 700:
            pygame.draw.rect(gameDisplay,(150,0,0),(900,600,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(250,0,0),(900,600,200,100),0)
        pygame.draw.rect(gameDisplay,(100,0,0),(900,600,200,100),5)
        text_surface, rect = font_35.render(("Vs. AI"), (0, 0, 0))
        gameDisplay.blit(text_surface, (950, 640))


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    mainMenu()
