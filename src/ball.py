import pygame
import random

class Ball(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.Surface((20,20))
    self.image.fill((255,255,255))
    self.rect = self.image.get_rect(center=pos)
    self.speed = 4
    self.moving = False
    self.rand_num = random.randint(-3, 3)
    self.direction = {'left': False, 'right': False, 'Up': False, 'Down': False}
    
  def initial_move(self):
    if not self.moving:
      self.rect.y += self.speed
      self.direction['Down'] = True
      self.moving = True
      
    # self.rect.x += self.rand_num
    # if self.rand_num < 0:
    #     self.direction['Left'] = True
  
  def set_direction(self):
    if self.direction['Down']:
      if self.rect.bottom >= 480:
        self.rect.bottom = 480
        self.direction['Down'] = False
        self.direction['Up'] = True
    elif self.direction['Up']:
      if self.rect.top <= 0:
        self.rect.top = 0
        self.direction['Up'] = False
        self.direction['Down'] =True   
        
      
  def move(self):
    if self.direction['Down']:
      self.rect.y += self.speed
    elif self.direction['Up']:
      self.rect.y -= self.speed
      
      
  def update(self):
    self.initial_move()
    self.set_direction()
    self.move()