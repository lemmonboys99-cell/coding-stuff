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

class Snake():
    def __init__(self): 
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARKBLUE, segment_rect,0,7)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)

screen = pygame.display.set_mode((cell_size*num_of_cells,cell_size*num_of_cells))
pygame.display.set_caption('SnakeGame1')
clock = pygame.time.Clock()

food = Food()
snake = Snake()
food_surface = pygame.image.load(".\\graphics\\food.png").convert_alpha()
scaled_food_surface = pygame.transform.scale(food_surface, (cell_size,cell_size))

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #checks if key is pressed
        if event.type == pygame.KEYDOWN:
            #checks if key is up arrow AND checks if the snake's direction is not the opposite so it doesn't run into itself
            if event.key == pygame.K_UP and snake.direction != Vector2(0,1):
                snake.direction = Vector2(0,-1)
            #the rest is self explanitory
            elif event.key == pygame.K_DOWN and snake.direction != Vector2(0,-1):
                snake.direction = Vector2(0,1)
            elif event.key == pygame.K_LEFT and snake.direction != Vector2(1,0):
                snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT and snake.direction != Vector2(-1,0):
                snake.direction = Vector2(1,0)

    #drawing
    screen.fill(BLUE)
    food.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(60)