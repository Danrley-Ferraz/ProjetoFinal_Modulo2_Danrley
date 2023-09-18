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
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "gameover.jpg"))
SPIDERVERSE = pygame.image.load(os.path.join(IMG_DIR, "spiderverse.jpg"))
SOUND = os.path.join(IMG_DIR, "Annihilate.mp3")


RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/correndo/correndo6.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/run6.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "miles/pulando/milespulando.png"))


JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/jump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/agachando/agachando2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/agachando/agachando1.png")),

]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/powerup/duck.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/venom/venom.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Miguel/miguel2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/carnificina/carnificina.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/lagarto/lagarto.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Rhyno/rhyno.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/sandman/sandman.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "miles/Norman/norman3.png")),

]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/portal1.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/bkged.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
