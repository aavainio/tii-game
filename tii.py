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
game_state = "start_menu"



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

def put_pos(grid_pos):
    global current_number, previous_position
    if not can_put_block(grid_pos):
        print("not legal")
        return
    previous_position = grid_pos
    pos = topixel(grid_pos)
    current_number +=1
    num=Number(pos, str(current_number))
    numbers.add(num)
    occupied.append(grid_pos)

def click_mouse():
    pos = pygame.mouse.get_pos()
    grid_pos = togrid(pos)
    put_pos(grid_pos)

def snap_grid(pos):
    x,y=pos
    return (x//GRID_SIZE*GRID_SIZE,y//GRID_SIZE*GRID_SIZE)

def togrid(pos):
    x,y=pos
    return (x//GRID_SIZE,y//GRID_SIZE)

def topixel(pos):
    x,y = pos
    return (x*GRID_SIZE,y*GRID_SIZE)

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

def create_obstacles(count, color, char):
    i = 0
    while i < count:
        print(i)
        x,y = get_free_tile()
        num = Number((x*GRID_SIZE,y*GRID_SIZE), char, color)
        numbers.add(num)
        occupied.append((x,y))
        i += 1

def get_free_tile():
    while True:
        x = random.randint(0, 15)
        y = random.randint(0, 14)
        if (x, y) in occupied:
            continue
        return x,y

def draw_start_menu():
    screen.fill((255,255,255))
    text_surface = font.render("press space to start:", 1, (0,0,0))
    screen.blit(text_surface, (10,10))

def handle_start_menu():
    global game_state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_state = "game"

create_obstacles(50, "blue", " ")
create_obstacles(10, "green", "$")
start_pos = get_free_tile()
put_pos(start_pos)




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            click_mouse()
    if game_state == "start_menu":
        draw_start_menu()
        handle_start_menu()

    elif game_state == "game":
        screen.fill((255,255,255))
        draw_grid()
        numbers.draw(screen)
    pygame.display.flip()