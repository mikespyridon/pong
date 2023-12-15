import pygame, sys
from src.paddle import Paddle
from src.ball import Ball

pygame.init()

#screen info
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

#clock info
FPS = 60
clock = pygame.time.Clock()

#objects
ball = Ball((WIDTH/2, HEIGHT/2))
paddle_right = Paddle('player', ((WIDTH - 20), (HEIGHT / 2)), 'white', ball.rect.y)
paddle_left = Paddle('computer', (20, (HEIGHT / 2)), 'green', ball.rect.y)


#groups
paddle_group = pygame.sprite.Group(paddle_left, paddle_right)
ball_group = pygame.sprite.GroupSingle(ball)

#score text
score = 0
text_font = pygame.font.SysFont('Arial', 30, True)
score_text = text_font.render(f'Score: {score}', True, 'white')
text_width = score_text.get_width()

#game loop
while True:
  
  screen.fill((0,0,0))
  screen.blit(score_text, (((WIDTH / 2) - (text_width / 2)), 25))
  
  paddle_group.update()
  ball_group.update()
  
  paddle_group.draw(screen)
  ball_group.draw(screen)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
  clock.tick(FPS)

      
    
    
