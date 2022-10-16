import pygame
from pygame.locals import * # type: ignore


class Plat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Platform.png')
        
        self.image = img
        self.rect = self.image.get_rect()
        
        