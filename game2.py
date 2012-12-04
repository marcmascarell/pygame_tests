import pygame
import random
from pygame import transform
from entities import Zombie

pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
time = pygame.time.Clock()

la_font = pygame.font.SysFont("Courier", 20, True, False)

info = la_font.render("Zombie Pyrty",0,(255,255,255))

zombie_list = []
cursor = pygame.Rect(0,0,1,1);

secondsint = 0

so = pygame.mixer.Sound("sound.wav")
so.play(-1)

last_divided = 0
coins = 50

zombie_surface = pygame.image.load('img/zombie.png')

for x in range(25):
    zombie = Zombie(screen, zombie_surface)
    zombie_list.append(zombie)

while running:

    time.tick(20)
    #print pygame.time.get_ticks()/1000
    secondsint = pygame.time.get_ticks()/1000
    seconds = str(secondsint)

    contador = la_font.render(seconds,0,(255,255,255))

    if (secondsint % 2) == 0 and secondsint > last_divided:
        last_divided = secondsint
        coins += 50

    show_coins = "$ " + str(coins)
    show_coins = la_font.render(show_coins,0,(255,255,255))

    cursor.center = pygame.mouse.get_pos()

    screen.fill((0,0,0))
    screen.blit(info, (20, 10))
    screen.blit(contador, (450, 10))
    screen.blit(show_coins, (250, 10))


    for zombie in zombie_list:
        zombie.render()

    pygame.draw.rect(screen,(200,20,20), cursor)
    pygame.display.update()



    left_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            left_click = True

    for zombie in reversed(zombie_list):
        zombie.frame(cursor, left_click)

pygame.quit()
