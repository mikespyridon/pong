import pygame, sys
from src.paddle import Paddle

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

FPS = 60
clock = pygame.time.Clock()

#objects
paddle_left = Paddle('computer', (20, (HEIGHT / 2)), 'green')
paddle_right = Paddle('player', ((WIDTH - 20), (HEIGHT / 2)), 'white')

paddle_group = pygame.sprite.Group(paddle_left, paddle_right)

while True:
  #update screen
  screen.fill((0,0,0))
  
  paddle_group.update()
  
  paddle_group.draw(screen)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
  clock.tick(FPS)

      
    
    
