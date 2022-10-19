import pygame
from pygame.locals import *
import sys
import random
 
from player import Player
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
bg = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
 

 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Platform.png')
        self.rect = self.image.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))

 
    def move(self):
        pass
 
PT1 = platform()
P1 = Player()

P1.rect.x = WIDTH / 2
P1.rect.y = HEIGHT / 2
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 

platforms = pygame.sprite.Group()
platforms.add(PT1)
 
 
def plat_gen():
    while len(platforms) < 7 :
        width = random.randrange(50,100)
        p  = platform()             
        p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)
 
 
 
for x in range(random.randint(5, 6)):
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)
 
while True: 
    displaysurface.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.jump()
   
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
    
    P1.update()
    plat_gen()
    for entity in all_sprites:
        displaysurface.blit(entity.image, entity.rect)
        entity.move()
 
    pygame.display.update()
   
    
    FramePerSec.tick(FPS)
    
    
    
    if P1.rect.y > HEIGHT:
        pygame.quit()
        
        
    
    
    
