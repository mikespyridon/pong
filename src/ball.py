import pygame
import random

class Ball(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.Surface((20,20))
    self.image.fill((255,255,255))
    self.rect = self.image.get_rect(center=pos)
    self.starting_pos = (640/2, 480/2)
    self.speed = 4
    
    self.moving = False
    self.collision = False
    
    self.direction = {'left': False, 'right': False, 'up': False, 'down': False}
    
    self.player_score = 0
    self.computer_score = 0
    
  def initial_move(self):
    rand_x = random.choice([1,2])
    rand_y = random.choice([-2,2])
    
    if not self.moving:
      if rand_y == -2:
        self.rect.y -= self.speed
        self.direction['up'] = True
      else:
        self.rect.y += self.speed
        self.direction['down'] = True
    
      if rand_x == 1:
        self.rect.x -= self.speed
        self.direction['left'] = True
      else:
        self.rect.x += self.speed
        self.direction['right'] = True
        
    self.moving = True
        
  def screen_bounce(self):
    if self.direction['down']:
      if self.rect.bottom >= 480:
        self.rect.bottom = 480
        self.direction['up'] = True
        self.direction['down'] = False
    elif self.direction['up']:
      if self.rect.top <= 0:
        self.rect.top = 0
        self.direction['up'] = False
        self.direction['down'] = True   
        
  def paddle_collision(self):
    direction = random.choice(['up', 'down'])
    if self.collision:
      self.speed = 4
      if self.direction['down']:
        self.direction[direction] = True
        if direction == 'down':
          self.direction['up'] = False
        else:
          self.direction['down'] = False
      elif self.direction['up']:
        self.direction[direction] = True
        if direction == 'up':
          self.direction['down'] = False
        else:
          self.direction['up'] = False
        
      self.collision = False
        
      if self.direction['left']:
        self.direction['left'] = False
        self.direction['right'] = True
        self.collision = False
        
      elif self.direction['right']:
        self.direction['right'] = False
        self.direction['left'] = True
        self.collision = False
        
  def move(self):
    if self.moving and not self.collision:
      if self.direction['down']:
        self.rect.y += self.speed
      if self.direction['up']:
        self.rect.y -= self.speed
      if self.direction['left']:
        self.rect.x -= self.speed
      if self.direction['right']:
        self.rect.x += self.speed
  
  def reset_directions(self):
    self.direction['right'] = False
    self.direction['left'] = False
    self.direction['up'] = False
    self.direction['down'] = False
  
  def reset_ball(self):
    if self.rect.left <= -200 and not self.collision:
      self.player_score += 1
      self.rect.center = self.starting_pos
      self.moving = False
      self.collision = False
      self.reset_directions()
  
    elif self.rect.right >= 800 and not self.collision:
      self.computer_score += 1
      self.rect.center = self.starting_pos
      self.moving = False
      self.collision = False
      self.reset_directions()
  
  def update(self):
    self.initial_move()
    self.move()
    self.screen_bounce()
    self.reset_ball()
    