import pygame
import random
import time

pygame.init()

diceImg1 = pygame.image.load('img1.png')
diceImg2 = pygame.image.load('img2.png')
diceImg3 = pygame.image.load('img3.png')
diceImg4 = pygame.image.load('img4.png')
diceImg5 = pygame.image.load('img5.png')
diceImg6 = pygame.image.load('img6.png')

def roll():
    number = random.randint(1,6)
    if number == 1:
        image1(xd,yd)
    elif number == 2:
        image2(xd,yd)
    elif number == 3:
        image3(xd,yd)
    elif number == 4:
        image4(xd,yd)
    elif number == 5:
        image5(xd,yd)
    elif number == 6:
        image6(xd,yd)
    pygame.display.update()
    return number
def image1(xd,yd):
    display.blit(diceImg1,(xd,yd))
    time.sleep(0.5)
def image2(xd,yd):
    display.blit(diceImg2,(xd,yd))
    time.sleep(0.5)
def image3(xd,yd):
    display.blit(diceImg3,(xd,yd))
    time.sleep(0.5)
def image4(xd,yd):
    display.blit(diceImg4,(xd,yd))
    time.sleep(0.5)
def image5(xd,yd):
    display.blit(diceImg5,(xd,yd))
    time.sleep(0.5)
def image6(xd,yd):
    display.blit(diceImg6,(xd,yd))
    time.sleep(0.5)

xd = 100
yd = 450

        
width=1280
height=720

green = (152,251,152)
black = (0,0,0)
blue=(0,0,255)

display=pygame.display.set_mode((width,height))
print(type(pygame.Surface))
pygame.display.set_caption("DICE GAME")
clock=pygame.time.Clock() 

player_one=pygame.image.load('playerTwo.png')
#pygame.Color(black)
display.fill(blue)

player_two=pygame.image.load('playerOne.png')

def player1(x,y):
    display.blit(player_one,(x,y))
def player2(x,y):
    display.blit(player_two,(x,y))
player_width=200
def game_loop():
    x = 35
    a=35
    y = (height*0.235)
    x_move = 0
    y_move = 0
    y1 = height*0.245
    margin = 2
    block_size = 35
    b = (height*0.374)
    b1 = (height*0.384)
    a_move=0
    b_move=0
    
    crash = False
    
    while not crash:
            #display.fill(blue)
            count=0
            x_move=0
            for x1 in range(40,width,40):
                rect=pygame.draw.rect(display,green,(x1+margin,y1,block_size,block_size),0)
            a_move=0
            for x2 in range(40,width,40):
                rect=pygame.draw.rect(display,green,(x2+margin,b1,block_size,block_size),0)
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crash = True
            
                if event.type == pygame.MOUSEBUTTONDOWN:                        
                    number = roll()
                    x_move = 40*number
                
                if event.type == pygame.MOUSEBUTTONUP:
                    x_move = 0

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_KP_ENTER:
                        number = roll()
                        a_move = 40*number
                if event.type==pygame.KEYUP:
                    a_move=0
            x += x_move
            player1(x,y)
            if x > width-player_width or x < 0:
                print('Player 1 won')
                crash = True

            a += a_move
            player2(a,b)
            if a > width-player_width or a < 0:
                print('Player 2 won')
                crash = True
            pygame.display.update()
            clock.tick(60)


game_loop()
pygame.quit()
quit()
