import random 

from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacles(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()


    def update(self, game_speed, obstacles):        
        self.rect.x -= game_speed       
        if self.rect.x < -self.rect.width:            
            obstacles.remove(self)
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)