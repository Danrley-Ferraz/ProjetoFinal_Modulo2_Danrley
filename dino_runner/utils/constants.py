import pygame
import os

# Global Constants
TITLE = "Spider-Man Miles: Velocity Vault"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "MilesWallpaper.png"))
MENU = pygame.image.load(os.path.join(IMG_DIR, "MenuWallpaper.jpg"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo6.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/agachando/agachando2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/agachando/agachando1.png")),

]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman3.png")),

]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/background.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
