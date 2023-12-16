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
paddle_right = Paddle('player', ((WIDTH - 20), (HEIGHT / 2)), 'white', ball)
paddle_left = Paddle('computer', (20, (HEIGHT / 2)), 'green', ball)

#groups
paddle_group = pygame.sprite.Group(paddle_left, paddle_right)
ball_group = pygame.sprite.GroupSingle(ball)

#score text
def draw_text(text):
  text_font = pygame.font.SysFont('Arial', 20, True)
  return text_font.render(text, True, 'white')

#game loop
while True:
  
  screen.fill((0,0,0))
  paddle_group.draw(screen)
  ball_group.draw(screen)
  
  paddle_group.update()
  ball_group.update()
  
  if pygame.sprite.spritecollide(ball, paddle_group, False):
    ball.speed = -ball.speed
    ball.collision = True
    ball.paddle_collision()
    
  computer_score_text = draw_text(f'Score: {ball.computer_score}')
  player_score_text = draw_text(f'Score: {ball.player_score}')
  
  screen.blit(computer_score_text, (10, 25))
  screen.blit(player_score_text, ((WIDTH - player_score_text.get_width()) - 10, 25))
  
  if ball.computer_score == 5 or ball.player_score == 5:
    ball.computer_score = 0
    ball.player_score = 0
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.update()
  clock.tick(FPS)

      
    
    
