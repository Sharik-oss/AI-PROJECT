import pygame
from pygame.locals import *
import sys
import random
 
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
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.jumping = False
        self.acc = vec(0,0)
        self.player_level = 0
 
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def jump(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, platforms, False)
        self.rect.y -= 2
        if hits:
            self.jumping = True
            self.vel.y = -15
 
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 10
                self.player_level += 1
                
    def is_colided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)
 
 
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
        
        
    
    
    
