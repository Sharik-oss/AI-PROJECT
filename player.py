import pygame
from pygame.locals import *# type: ignore
import sys



vec = pygame.math.Vector2
ani = 4

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        img = pygame.image.load('Player.png')
        self.image = img
        self.rect = self.image.get_rect()
    
    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex# type: ignore
        self.rect.y = self.rect.y + self.movey# type: ignore

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
                
    def gravity(self):
        self.movey += 0.1

    def jump(self):
        self.movey -= 10

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
