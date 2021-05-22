import pygame
import sys
import random
import time
pygame.init()
Width = 800
Height = 600
Red = (255, 0, 0)
Blue = (0, 0, 255)
Yellow = (255,255,0)
Green = (0,128,0)
Speed = 10
White = (255, 255, 255)
backgroundColor = (0, 0, 0)
playerSize = 40
playerPos = [100, 300]
columnSize1 = 50
columnSize2 = 150
columnPos1 = [random.randint(0,Width-playerSize), 0]
columnPos2 = [random.randint(0,Width-playerSize), 0]
columnPos3 = [random.randint(0,Width-100), 0]
columnPos4 = [random.randint(0,Width-100), 0]
screen = pygame.display.set_mode((Width, Height))
game_over = False
Score = 0
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)

def set_level(Score, Speed):
    if Score < 15:
        Speed = 15
    elif Score < 30:
        Speed = 20
    elif Score < 50:
        Speed = 25
    else:
        Speed = 30
    return Speed
    # SPEED = score/5 + 1

def detect_collision(playerPos, columnPos1):
    p_x = playerPos[0]
    p_y = playerPos[1]
    c1_x = columnPos1[0]
    c1_y = columnPos1[1]
    if (c1_y >= p_y and c1_y < (p_y + 50)) or (p_y >= c1_y and p_y < (c1_y+150)):
        if (c1_x >= p_x and c1_x < (p_x + playerSize)) or (p_x >= c1_x and p_x < (c1_x+playerSize)):
           return True
    return False

def detect_collision(playerPos, columnPos2):
    p_x = playerPos[0]
    p_y = playerPos[1]
    c2_x = columnPos2[0]
    c2_y = columnPos2[1]
    if (c2_y >= p_y and c2_y < (p_y + 50)) or (p_y >= c2_y and p_y < (c2_y+150)):
        if (c2_x >= p_x and c2_x < (p_x + playerSize)) or (p_x >= c2_x and p_x < (c2_x+playerSize)):
           return True
    return False

def detect_collision(playerPos, columnPos3):
    p_x = playerPos[0]
    p_y = playerPos[1]
    c3_x = columnPos3[0]
    c3_y = columnPos3[1]
    if (c3_y >= p_y and c3_y < (p_y + 50)) or (p_y >= c3_y and p_y < (c3_y+150)):
        if (c3_x >= p_x and c3_x < (p_x + playerSize)) or (p_x >= c3_x and p_x < (c3_x+playerSize)):
           return True
    return False

def detect_collision(playerPos, columnPos4):
    p_x = playerPos[0]
    p_y = playerPos[1]
    c4_x = columnPos4[0]
    c4_y = columnPos4[1]
    if (c4_y >= p_y and c4_y < (p_y + 50)) or (p_y >= c4_y and p_y < (c4_y+150)):
        if (c4_x >= p_x and c4_x < (p_x + playerSize)) or (p_x >= c4_x and p_x < (c4_x+playerSize)):
           return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            x = playerPos[0]
            y = playerPos[1]
            if event.key == pygame.K_UP:
                y -= 40
            elif event.key == pygame.K_DOWN:
                y += 40
            
            playerPos = [x,y]
    screen.fill(backgroundColor)
    if columnPos1[0] >= 0 and columnPos1[0] < Width and columnPos2[0] >= 0 and columnPos2[0] < Width:
        columnPos1[0] -= Speed
        columnPos2[0] -= Speed
    else:
        columnPos1[0] = 700
        columnPos2[0] = 700
        Score += 1 
        columnPos1[1] = random.randint(0,random.randint(0,50))
        columnPos2[1] = random.randint(0,random.randint(450,550))
    if columnPos3[0] >= 0 and columnPos3[0] < Width and columnPos4[0] >= 0 and columnPos4[0] < Width:
        columnPos3[0] -= Speed
        columnPos4[0] -= Speed
    else:
        columnPos3[0] = 799
        columnPos4[0] = 799
        Score += 1 
        columnPos3[1] = random.randint(0,random.randint(0,50))
        columnPos4[1] = random.randint(0,random.randint(450,550))
    Speed = set_level(Score, Speed)
    text = "Score:" + str(Score)
    label = myFont.render(text, 1, Yellow)
    screen.blit(label, (Width-200, Height-40))
    if detect_collision(playerPos,columnPos1):
        game_over = True
    if detect_collision(playerPos,columnPos2):
        game_over = True
    if detect_collision(playerPos,columnPos3):
        game_over = True
    if detect_collision(playerPos,columnPos4):
        game_over = True
    pygame.draw.rect(screen, Red, (playerPos[0], playerPos[1], playerSize, playerSize))
    pygame.draw.rect(screen, Green, (columnPos1[0], columnPos1[1], columnSize1, columnSize2)) 
    pygame.draw.rect(screen, Green, (columnPos2[0], columnPos2[1], columnSize1, columnSize2)) 
    pygame.draw.rect(screen, Green, (columnPos3[0], columnPos3[1], columnSize1, columnSize2)) 
    pygame.draw.rect(screen, Green, (columnPos4[0], columnPos4[1], columnSize1, columnSize2)) 
    clock.tick(30)
    pygame.display.update()