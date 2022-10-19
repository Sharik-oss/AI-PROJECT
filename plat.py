import pygame
from pygame.locals import * # type: ignore\
import random

HEIGHT = 533
WIDTH = 400
class Plat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Platform.png')
        img = pygame.transform.scale(img, (68, 14))
        
        self.image = img
        self.rect = self.image.get_rect(center = (random.randint(0, WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
        
        