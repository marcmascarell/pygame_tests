import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True
time = pygame.time.Clock()

la_font = pygame.font.SysFont("Arial", 16, True, False)

info = la_font.render("Tienes 10 segundos",0,(255,255,255))

listarec = []
r1 = pygame.Rect(0,0,1,1);

seconds = 0

so = pygame.mixer.Sound("sound.wav")
so.play(-1)



for x in range(25):
    w = random.randrange(10,30)
    h = random.randrange(10,40)
    x = random.randrange(450)
    y = random.randrange(450)
    listarec.append(pygame.Rect(x, y, w, h))

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for recs in listarec:
                if r1.colliderect(recs):
                    recs.width = 0
                    recs.height = 0

    time.tick(20)
    print pygame.time.get_ticks()/1000
    seconds = pygame.time.get_ticks()/1000
    seconds = str(seconds)
    contador = la_font.render(seconds,0,(0,0,230))

    screen.blit(info, (100, 10))
    screen.blit(contador, (400, 10))
    (r1.center) = pygame.mouse.get_pos()

    screen.fill((0,0,0))
    for recs in listarec:
        pygame.draw.rect(screen,(0,200,0), recs)
    pygame.draw.rect(screen,(200,20,20), r1)
    pygame.display.update()

pygame.quit()
