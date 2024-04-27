import pygame
pygame.init()
class Snake:
    def __init__(self) -> None:
        self.Snake = []
        self.added_block = None
        self.Snake.append(pygame.Rect(0,0,50,50))
    def new(self):
        return self.Snake
    def move(self, snake : list, x,y):
        if self.added_block != None:
            self.added_block.x = snake[len(snake)-1].x
            self.added_block.y = snake[len(snake)-1].y

        for i in range(len(snake)-1, -1, -1):
            if i == 0:
                snake[i].x += x
                snake[i].y += y
            else:
                snake[i].x = snake[i-1].x
                snake[i].y = snake[i-1].y
        snake.append(self.added_block)
    def add(self, snake: list):
        self.added_block = pygame.Rect(0,0,50,50)
game = True
win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
snake = Snake().new()
frame = 0
x = 0
y = 0
while game:
    frame += 1
    win.fill('orange')
    clock.tick(60)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x = -50
        y = 0
    if keys[pygame.K_d]:
        x = 50
        y = 0
    if keys[pygame.K_w]:
        y = -50
        x = 0
    if keys[pygame.K_s]:
        y = 50
        x = 0
    if keys[pygame.K_e]:
        Snake().add(snake)
    if frame % 30 == 0:
        Snake().move(snake, x, y)
    for i in snake:
        
        pygame.draw.rect(win, 'light green', i)
  
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
