import pygame,sys,random
from pygame.math import Vector2

pygame.init()

BLUE = (80, 133, 188)
DARKBLUE = (8,96,168)

cell_size = 30 
num_of_cells = 25

class Food():
    def __init__(self):
        self.position = self.gen_random_pos()

    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size )#x,y,w,h of rect
        screen.blit(scaled_food_surface, food_rect)

    def gen_random_pos(self):
        X = random.randint(0, num_of_cells-1)
        Y = random.randint(0, num_of_cells-1)
        pos = Vector2(X,Y)
        return pos
screen = pygame.display.set_mode((cell_size*num_of_cells,cell_size*num_of_cells))
pygame.display.set_caption('SnakeGame1')
clock = pygame.time.Clock()

food = Food()
food_surface = pygame.image.load(".\\graphics\\food.png").convert_alpha()
scaled_food_surface = pygame.transform.scale(food_surface, (cell_size,cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #drawing
    screen.fill(BLUE)
    food.draw()
    pygame.display.update()
    clock.tick(60)