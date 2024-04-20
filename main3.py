'''
Бажано загрузити проект в Visual Studio,
Оскільки тут відтворюється дивно та можливо фонт Calibri не загружений...
'''







import pygame

import random

import time

from random import randint



pygame.init()

win = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Клікер')
clock = pygame.time.Clock()
clicks = 0




text2 = pygame.font.SysFont('Calibri', 25).render('Нажми!', True, (0,0,0))


rects = [
    pygame.Rect(120, 250, 100, 300),
    pygame.Rect(340, 250, 100, 300),
    pygame.Rect(560, 250, 100, 300),
    pygame.Rect(780, 250, 100, 300)
]
def advanced_choice(obj : list, previous):

    
    while True:
        a2 = random.choice(obj)
        if a2 != previous:
            break

    return a2
click_rects = []
text = pygame.font.SysFont('Calibri', 50).render("Кількість нажатих блоків: " + str(clicks) + "/10", True,  (0,0,0))
game = True
debounce = False
winn = False


color = (255,255,255)
click_color = (255, 0, 0)

frames = 0

a = random.choice(rects)
rects.remove(a)
click_rects.append(a)

randomoffset = randint(2, 4) * 30

start = time.time()

while game:
    clock.tick(60)
    frames += 1
    if frames == randomoffset and not winn: #didnt click in time
        if a in click_rects:
            click_rects.remove(a)
        rects.append(a)
        
        clicks -= 1
        text = pygame.font.SysFont('Calibri', 50).render("Кількість нажатих блоків: " + str(clicks) + "/10", True,  (0,0,0))
        a = advanced_choice(rects, a)
        rects.remove(a)
        click_rects.append(a)
        frames = 0
        randomoffset = randint(45, 60)
    if time.time() - start > 10 and not winn:
        print(time.time() - start)
        game = False

        
        
    



    win.fill((225,221,137))

    win.blit(text, (200,150))


    for i in rects:
        pygame.draw.rect(win, (color), i)
        pygame.draw.rect(win, (0,0,0), i, 5)
    for i in click_rects:
        pygame.draw.rect(win, (click_color), i)
        pygame.draw.rect(win, (0,0,0), i, 5)
        if pygame.mouse.get_pressed(3)[0] == True and i.x < pygame.mouse.get_pos()[0] < (i.x+100) and i.y < pygame.mouse.get_pos()[1] < (i.y+300) and i in click_rects and not winn:
            # clicked on time
            if i in click_rects:
                click_rects.remove(i)
                clicks += 1
            if i not in rects:
                rects.append(i)
            randomoffset = randint(45, 60)
            frames = 0
            if clicks == 10:
                winn = True
                color = (0,255,0)
                click_color = (0, 255, 0)
            text = pygame.font.SysFont('Calibri', 50).render("Кількість нажатих блоків: " + str(clicks) + "/10", True,  (0,0,0))
            a = advanced_choice(rects, i)
            rects.remove(a)
            click_rects.append(a)  
            
            print(clicks)
    
        
    if not winn:
        win.blit(text2, (click_rects[0].x+10, click_rects[0].y+132.5))

        



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
