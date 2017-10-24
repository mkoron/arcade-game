import sys, pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = weight_image
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()

pygame.init()
screen_size = 1024, 680
pygame.display.set_mode(screen_size, FULLSCREEN)
pygame.mouse.set_visible(0)

weight_image = pygame.image.load('images/weight.png')
weight_image = weight_image.convert() 

sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight())

screen = pygame.display.get_surface()
white = (255, 255, 255)
screen.fill(white)
pygame.display.flip()

# Used to erase the sprites - Taken from the code of the 3rd edition
def clear_callback(surf, rect):
    surf.fill(white, rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        sprites.clear(screen, clear_callback)
        sprites.update()
        updates = sprites.draw(screen)
        pygame.display.update(updates)
