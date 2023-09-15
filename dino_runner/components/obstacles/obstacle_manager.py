import random
import pygame 

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.when_appars = 0
    
    def generate_cactus(self):
        if len(self.obstacles) == 0:
            self.when_appars
