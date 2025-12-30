import pygame
import random
import math

pygame.init()
def hit( x, y, cx, cy):
    distance = math.sqrt(math.pow(x-cx,2) + math.pow(y-cy,2))
    if distance < 75:
        return True
    else:
        return False 


width = 800
height = 600
game_name = "car dash "
x = 400
y = 500
sizex = 50
sizey = 70
movement = 100
score = 0
yellow = (255, 255, 102)
blue = (50, 153, 213)
red = (213, 50, 80)
lx = 150
ly = 0

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(game_name)
clock = pygame.time.Clock()
enemy = pygame.image.load("image/em.png")
enemyca = pygame.transform.scale(enemy,(100,140))

player = pygame.image.load("image/pl.png")
player_car = pygame.transform.scale(player,(100,140))

road = pygame.image.load("image/bg.jpg")
bg = pygame.transform.scale(road,(800,600))



no_of_car = 4
CX = 50
enemycar = []
cx = []
cy = []
car_movement = []
for i in range(no_of_car):
    enemycar.append(enemyca)
    cx.append(CX)
    cy.append(random.randint(-400,-200))
    car_movement.append(2)
    CX += 200

font = pygame.font.SysFont(None, 35)
start = True
game_close = False
while start:
    while game_close:
        screen.fill(blue)
        msg = font.render("Game Over! Press SPACE-Play Again or Q-Quit", True, red)
        screen.blit(msg, [width / 10, height / 3])
        screen.blit(value, [300,250])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    start = False
                    game_close = False
                if event.key == pygame.K_SPACE:
                    for i in range(no_of_car):
                        cx.append(CX)
                        cy.append(random.randint(-400,-200))
                        CX -= 150
                    x = random.randint(50,750)
                    score = 0
                    game_close = False 
    screen.blit(bg,(0,0))
    # screen.fill((255, 255 , 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x -= movement
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += movement
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y -= movement
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += movement    
    if y >= 550:
        y -= movement
    if y <= -50:
        y += movement
    if x >= 750 :
        x -= movement   
    if x <= -75:
        x += movement 

    for i in range(no_of_car):
        if cy[i] >= 600:
            cy[i] += 5
            cy[i] = random.randint(-400,0) 
            score += 1           
        cy[i] += car_movement[i]
        screen.blit(enemycar[i],(cx[i], cy[i]))
        # pygame.draw.rect(screen,(0 , 0 , 255),(cx[i] , cy[i] ,sizex , sizey))
        hits = hit(x , y , cx[i] ,cy[i])
        if hits:
            game_close = True
    # pygame.draw.rect(screen , (255 , 0 , 0),(x,y,sizex,sizey))
    # pygame.draw.line()
    screen.blit(player_car,(x,y))
    value = font.render("Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])
    pygame.display.update()
    clock.tick(60) 
pygame.quit()               
