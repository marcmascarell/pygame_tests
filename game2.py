import pygame
import random
from pygame import transform

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
time = pygame.time.Clock()

la_font = pygame.font.SysFont("Courier", 20, True, False)

info = la_font.render("Zombie Pyrty",0,(255,255,255))

listarec = []
r1 = pygame.Rect(0,0,1,1);

secondsint = 0

so = pygame.mixer.Sound("sound.wav")
so.play(-1)

last_divided = 0
coins = 50

zombie = pygame.image.load('img/zombie.png')

for x in range(25):
    w = random.randrange(10,30)
    h = random.randrange(10,40)

    x = random.randrange(450)
    y = random.randrange(20,450)
    listarec.append(pygame.Rect(x, y, w, h))

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for recs in listarec:
                if r1.colliderect(recs):
                    #recs.width = 0
                    #recs.height = 0
                    listarec.remove(recs)

    time.tick(20)
    #print pygame.time.get_ticks()/1000
    secondsint = pygame.time.get_ticks()/1000
    seconds = str(secondsint)

    contador = la_font.render(seconds,0,(255,255,255))

    if (secondsint % 2) == 0 and secondsint > last_divided:
        last_divided = secondsint
        coins = coins + 50

    show_coins = "$ " + str(coins)
    show_coins = la_font.render(show_coins,0,(255,255,255))

    r1.center = pygame.mouse.get_pos()

    screen.fill((0,0,0))
    screen.blit(info, (20, 10))
    screen.blit(contador, (450, 10))
    screen.blit(show_coins, (250, 10))


    for recs in listarec:
        recs[0] += 1
        #pygame.draw.rect(screen,(0,200,0), recs)
        screen.blit(transform.scale(zombie, recs[2:]), recs)

    pygame.draw.rect(screen,(200,20,20), r1)
    pygame.display.update()

pygame.quit()
