import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)           
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)        #generates random positions for the apple, but only in multiples of 10 (to be aligned with the snake)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])  #snake and apple collision

UP = 0
RIGHT = 1
DOWN = 2               #movement directions
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))       #creates a window for the game (tuple)
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]     #creates snake
snake_skin = pygame.Surface((10,10))      #define pixel size
snake_skin.fill((255,255,255))        #snake color

apple_pos = on_grid_random()      
apple = pygame.Surface((10,10))        #pixel size
apple.fill((255,0,0))                #apple color

my_direction = LEFT                    #start the snake from the left

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',18)
score = 0

game_over = False
while not game_over:                            #infinite loop of the game
    clock.tick(10)                #limits the speed of the snake
    for event in pygame.event.get():      #takes everything the user does
        if event.type == QUIT:          
            pygame.quit()             #close game event
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN        #keyboard keys move snake
            if event.key == K_LEFT:        
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()    #generates a new position for apple
        snake.append((0,0))                 #the snake grows
        score = score + 1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):              #consolidates the movement with the tail
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)      
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:                             #gives functionality to movements by changing head position
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))                #clears the screen before the game
    screen.blit(apple, apple_pos)          #plot the apple

    for x in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:                      
        screen.blit(snake_skin,pos)     #plot the snake

    pygame.display.update()           #screen keeps updating

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
