import pygame

class Paddle(pygame.sprite.Sprite):
  def __init__(self, type, pos, fill):
    super().__init__()
    self.image = pygame.Surface((20, 100))
    self.fill = self.image.fill(fill)
    self.rect = self.image.get_rect(center=pos)
    self.type = type
    self.pos = pos
    
  
  def get_input(self):
    keys = pygame.key.get_pressed()
    
    if self.type == 'player':
      if keys[pygame.K_UP]:
        self.rect.y -= 5
      elif keys[pygame.K_DOWN]:
        self.rect.y += 5
  
  def screen_constraint(self):
    if self.rect.top <= 0:
      self.rect.top = 0
    elif self.rect.bottom >= 480:
      self.rect.bottom = 480
    
  
  def update(self):
    self.get_input()
    self.screen_constraint()