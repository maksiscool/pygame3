import pygame
import random
import time
import threading
from random import randint


pygame.init()
win = pygame.display.set_mode((1376, 768))
game = True
first = 0
second = 0
third = 0
player1 = pygame.Rect(randint(300, 1300), randint(200, 700), 50, 50)
clock = pygame.time.Clock()
def idk():
    global first
    global second
    global third
    while game:
        for i in range(255):
            first += 1
            time.sleep(0.01)
            if not game:
                break
        for i in range(255):
            second += 1
            time.sleep(0.01)
            if not game:
                break
        for i in range(255):
            third += 1
            time.sleep(0.01)
            if not game:
                break
        for i in range(255):
            first -= 1
            time.sleep(0.01)
            if not game:
                break
        for i in range(255):
            second -= 1
            time.sleep(0.01)
            if not game:
                break
        for i in range(255):
            third -= 1
            time.sleep(0.01)
            if not game:
                break
threading.Thread(target=idk).start()

menaces = []
menaces2 = []
time1 = 0.5
def cubecreate():
    global time1
    time.sleep(3)
    while True:

        time.sleep(time1)
        menaces.append(pygame.Rect(random.randint(0, 1346), -30, 30, 30))

        time1 *= 0.98
        if not game:
            break

        time.sleep(time1)
        menaces2.append( pygame.Rect(-30, random.randint(0, 738), 30, 30))

        time1 *= 0.98
        if not game:
            break



threading.Thread(target=cubecreate).start()

while game:
    win.fill((first, second, third))
    for b in menaces:
        pygame.draw.rect(win, (0, 0, 0), b)
        b.y += 15
        if b.colliderect(player1):
            game = False
        if b.y > 738:
            menaces.remove(b)
    for b in menaces2:
        pygame.draw.rect(win, (0, 0, 0), b)
        b.x += 15
        if b.colliderect(player1):
            game = False
        if b.x > 1346:
            menaces2.remove(b)
    

    clock.tick(60)
    

    win.blit(pygame.font.SysFont(None, 50).render("Press Q to leave", True, "white"), (550, 350))

    pygame.draw.rect(win, (0,0,255), player1)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player1.x >= 6:
            player1.x -= 6
    if keys[pygame.K_d]:
        if player1.x <= 1320:
            player1.x += 6
    if keys[pygame.K_w]:
        if player1.y >= 6:
            player1.y -= 3
    if keys[pygame.K_s]:
        if player1.y <= 712:
            player1.y += 6
    if keys[pygame.K_q]:
        game = False

    
