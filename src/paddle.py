import pygame
from src.ball import Ball
import math

class Paddle(pygame.sprite.Sprite):
  def __init__(self, type, pos, fill, ball):
    super().__init__()
    self.image = pygame.Surface((20, 100))
    self.fill = self.image.fill(fill)
    self.rect = self.image.get_rect(center=pos)
    self.type = type
    self.pos = pos
    self.ball = ball
    
    self.speed = 0
    
  def get_input(self):
    keys = pygame.key.get_pressed()
    
    if self.type == 'player':
      if keys[pygame.K_UP]:
        self.rect.y -= 4
      elif keys[pygame.K_DOWN]:
        self.rect.y += 4
  
  def screen_constraint(self):
    if self.rect.top <= 0:
      self.rect.top = 0
    elif self.rect.bottom >= 480:
      self.rect.bottom = 480
      
  def computer_paddle_movement(self, ball):
    
    if self.type == 'computer':
     if ball.direction['left'] and self.ball.rect.x > 0:
        self.rect.y = self.ball.rect.y * .5
    
  def update(self):
    self.get_input()
    self.computer_paddle_movement(self.ball)
    self.screen_constraint()