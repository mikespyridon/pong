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

#groups
paddle_group = pygame.sprite.Group(paddle_left, paddle_right)

#score text
score = 0
text_font = pygame.font.SysFont('Arial', 30, True)
score_text = text_font.render(f'Score: {score}', True, 'white')
text_width = score_text.get_width()

while True:
  #update screen
  screen.fill((0,0,0))
  screen.blit(score_text, (((WIDTH / 2) - (text_width / 2)), 25))
  
  paddle_group.update()
  
  paddle_group.draw(screen)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
  clock.tick(FPS)

      
    
    
