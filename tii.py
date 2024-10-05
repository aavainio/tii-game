import sys

import pygame
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 40
current_number = 1



class Number(pygame.sprite.Sprite):
    def __init__(self,pos,text):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        text_surface = font.render(text,1,(255,255,255))
        self.image.fill((0, 0, 0))
        self.image.blit(text_surface, (0,5))
        self.rect=self.image.get_rect()
        self.rect.topleft=(pos)

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font=pygame.font.Font(pygame.font.get_default_font(),36)

numbers=pygame.sprite.Group()
numbers.add(Number((15,15), "1"))

def draw_grid():
    for x in range(0,SCREEN_WIDTH,GRID_SIZE):
        pygame.draw.line(screen, (0,0,0),(x,0),(x,SCREEN_HEIGHT))
    for y in range(0,SCREEN_HEIGHT,GRID_SIZE):
        pygame.draw.line(screen, (0,0,0),(0,y),(SCREEN_WIDTH, y))

def click_mouse():
    global current_number
    pos=pygame.mouse.get_pos()
    pos = snap_grid(pos)
    current_number +=1
    num=Number(pos, str(current_number))
    numbers.add(num)

def snap_grid(pos):
    x,y=pos
    return (x//GRID_SIZE*GRID_SIZE,y//GRID_SIZE*GRID_SIZE)

def togrid(pos):
    x,y=pos
    return (x//GRID_SIZE,y//GRID_SIZE)



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