import random
import pygame

from dino_runner.utils.constants import SOUND

class Music:
    def __init(self):
        pygame.mixer.init()

    
    def play_music(self):
        self.music = SOUND
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(0)
    
    def play_sound(self, sound, volume):
        self.sons = pygame.mixer.Sound(sound)
        self.sons.set_volume(volume)
        self.sons.play()