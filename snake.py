import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)           
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)        #gera posições aleatórias para a maçã, mas em apenas múltiplos de 10(para ficar alinhado com a snake)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])  #colisão snake e maçã

UP = 0
RIGHT = 1
DOWN = 2               #direções dos movimentos
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))       #cria uma tela para o jogo (tupla)
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]     #cria snake
snake_skin = pygame.Surface((10,10))      #define tamanho dos pixels
snake_skin.fill((255,255,255))        # cor da snake

apple_pos = on_grid_random()      
apple = pygame.Surface((10,10))        #tamanho dos pixels
apple.fill((255,0,0))                # cor da maçã

my_direction = LEFT                    #inicia a snake pela esquerda

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf',18)
score = 0

game_over = False
while not game_over:                            #laço infinito do jogo
    clock.tick(10)                #limita a velocidade da snake
    for event in pygame.event.get():      #pega tudo oq o usuário faz
        if event.type == QUIT:          
            pygame.quit()             #evento de fechar jogo
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN        #teclas do teclado movimenta snake 
            if event.key == K_LEFT:        
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()    #gera uma nova posição para maçã
        snake.append((0,0))                 #aumenta a snake
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
    
    for i in range(len(snake) - 1, 0, -1):              #consolida o movimento mexendo com o rabo
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)      
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:                             #da funcionalidade aos movimentos mudando posição da cabeça
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))                # limpa a tela antes do jogo
    screen.blit(apple, apple_pos)          #plota a maçã

    for x in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:                      
        screen.blit(snake_skin,pos)     #plota a snake

    pygame.display.update()           #tela fica atualizando sempre

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

