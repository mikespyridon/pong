import pygame, sys

pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

FPS = 60
clock = pygame.time.Clock()

while True:
  
  screen.fill((0,0,0))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  
  pygame.display.update()
  clock.tick(FPS)

      
    
    
