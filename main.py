import pygame,sys
from pygame.math import Vector2

pygame.init()

BLUE = (80, 133, 188)
DARKBLUE = (8,96,168)

cell_size = 30 
num_of_cells = 25


class Food:
    def __init__(self):
        self.position = Vector2(5,6)
    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size )#x,y,w,h of rect.
        pygame.draw.rect(screen, DARKBLUE, food_rect)


screen = pygame.display.set_mode((cell_size*num_of_cells,cell_size*num_of_cells))

pygame.display.set_caption('SnakeGame1')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLUE)
    pygame.display.update()
    clock.tick(60)