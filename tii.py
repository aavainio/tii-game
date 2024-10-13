import sys
import random
from venv import create

import pygame
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 40
current_number = 0
previous_position = None
occupied = []



class Number(pygame.sprite.Sprite):
    def __init__(self,pos,text, bgcolor = (0,0,0)):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        text_surface = font.render(text,1,(255,255,255))
        self.image.fill((bgcolor))
        self.image.blit(text_surface, (0,5))
        self.rect=self.image.get_rect()
        self.rect.topleft=(pos)

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font=pygame.font.Font(pygame.font.get_default_font(),36)

numbers=pygame.sprite.Group()
#numbers.add(Number((15,15), "1"))

def draw_grid():
    for x in range(0,SCREEN_WIDTH,GRID_SIZE):
        pygame.draw.line(screen, (0,0,0),(x,0),(x,SCREEN_HEIGHT))
    for y in range(0,SCREEN_HEIGHT,GRID_SIZE):
        pygame.draw.line(screen, (0,0,0),(0,y),(SCREEN_WIDTH, y))

def click_mouse():
    global current_number, previous_position
    pos=pygame.mouse.get_pos()
    grid_pos = togrid(pos)
    if not can_put_block(grid_pos):
        print("not legal")
        return
    previous_position = grid_pos
    pos = snap_grid(pos)
    current_number +=1
    num=Number(pos, str(current_number))
    numbers.add(num)
    occupied.append(grid_pos)

def snap_grid(pos):
    x,y=pos
    return (x//GRID_SIZE*GRID_SIZE,y//GRID_SIZE*GRID_SIZE)

def togrid(pos):
    x,y=pos
    return (x//GRID_SIZE,y//GRID_SIZE)

def can_put_block(pos):
    if pos in occupied:
        return False
    print(pos, previous_position)
    if previous_position is None:
        return True
    x,y = pos
    px,py = previous_position
    dx = abs(x-px)
    dy = abs(y-py)
    if dx==3 and dy==0:
        return True
    if dy==3 and dx==0:
        return True
    if dx==2 and dy==2:
        return True
    return False

def create_obstacles(count):
    for i in range(count):
        print(i)
        x = random.randint(0,15)
        y = random.randint(0,14)
        num = Number((x*GRID_SIZE,y*GRID_SIZE), " ", "blue")
        numbers.add(num)
        occupied.append((x,y))


create_obstacles(5)




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            click_mouse()
    screen.fill((255,255,255))
    draw_grid()
    numbers.draw(screen)
    pygame.display.flip()