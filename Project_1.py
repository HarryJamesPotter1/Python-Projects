import pygame

S_WIDTH = 800
S_HEIGHT = 800
COLS = 10
ROWS = 20
B_WIDTH = S_WIDTH // COLS
B_HEIGHT = S_HEIGHT // ROWS
SPEED = 100
COLORS = [(213, 62, 79), (244, 109, 67), (253, 174, 97), (254, 224, 139), (255, 255, 191), (230, 245, 152), (171, 221, 164), (102, 194, 165),
          (50, 136, 189), (102, 194, 165), (171, 221, 164), (230, 245, 152), (255, 255, 191), (254, 224, 139), (253, 174, 97), (244, 109, 67)]


#initialize pygame
pygame.init()

#screen setup
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))

pygame.display.set_caption("Stacks")

left = 0
width = S_HEIGHT
right = left + S_WIDTH

prev_left = left
prev_right = right
prev_width = width

y = S_HEIGHT - B_HEIGHT
direction = 'l'
score = 0
max_score = 0
speed = SPEED
color = COLORS[0]

loop = True

while loop:
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    #on each tick render the score and max score
    screen.fill((0,0,0), (0, 0, S_WIDTH, B_HEIGHT))
    font = pygame.font.SysFont('Arial Black', 30)
    text = font.render("Score: " + str(score) + "    Max: " + str(max_score),True,(255,255,255))

    screen.blit(text, (S_WIDTH // 2 - 120, 2))
    
    #Get keys pressed
    keys = pygame.key.get_pressed()
    #handle keys pressed
    if keys[pygame.K_SPACE]:

        #if we miss the stack, then the game is over
        if right <= prev_left or left >= prev_right:
            pygame.time.delay(1000)
            screen.fill((0,0,0))
            score = 0
            left = 0
            width = S_WIDTH
            right = left + S_WIDTH
            prev_left = left
            prev_right = right
            prev_width = prev_width
            y = S_HEIGHT - B_HEIGHT
            direction = 'l'
            speed = SPEED
            color = COLORS[0]
        else:
            #cut the block if it misses the edge
            if left != prev_left:
                left = max(left,prev_left)
                right = min(right,prev_right)
                width = right - left

                
            score += 1
            max_score = max(score, max_score)

            #save current coordinates
            prev_left = left
            prev_right = right
            prev_width = width
            screen.fill((0,0,0),(0,y,S_WIDTH,B_HEIGHT))
            pygame.draw.rect(screen, color, (left, y, width, B_HEIGHT))

            if y - B_HEIGHT != B_HEIGHT:
                y -= B_HEIGHT
                color = COLORS[score % len(COLORS)]
            
            else:
                screen.fill((0,0,0))
                pygame.draw.rect(screen, color, (left, S_HEIGHT - B_HEIGHT, prev_width, B_HEIGHT))
                color = COLORS[score % len(COLORS)]
                y = S_HEIGHT - 2 * B_HEIGHT
                speed = int(speed*0.97)
    
    #Move rectangle side to side
    screen.fill((0,0,0),(0,y,S_WIDTH,B_HEIGHT))

    if left < 0 - width + 2 * B_WIDTH:
        direction = 'r'
    
    elif left > S_WIDTH - 2 * B_WIDTH:
        direction = 'l'

    if direction == 'r':
        left += B_WIDTH
        right += B_WIDTH

    elif direction == 'l':
        left -= B_WIDTH
        right -= B_WIDTH

    pygame.draw.rect(screen,color, (left, y, width, B_HEIGHT))

    pygame.display.update()

pygame.quit()

        

    
