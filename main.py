import random as rand
import pygame
from pygame.locals import *

from player import Player
from plat import Plat

pygame.init()


width = 400
height = 533
score = 0
fps = 60


framePerSec = pygame.time.Clock()

window = pygame.display.set_mode((width, height))
bg = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg, (width, height))


running = True
player = Player()
player.rect.x = width / 2  # type: ignore
player.rect.y = height / 2  # type: ignore
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10


platform = Plat()
platform.rect.x = rand.randint(0, width - 50)
platform.rect.y = height - 50
platform_list = pygame.sprite.Group()
platform_list.add(platform)

while running:
    window.blit(bg, (0, 0))
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_SPACE:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

    if player.is_collided_with(platform):
            player.jump()
            score +=1
            print(score)

    player.gravity()
    player.update()
    player_list.draw(window)
    platform_list.draw(window)
    framePerSec.tick(fps)
    pygame.display.update()
    if int(player.rect.y) > height:
        running = False
    
pygame.quit()