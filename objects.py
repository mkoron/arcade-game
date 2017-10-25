import pygame
import os
import config
from random import randrange


class SquishSprite(pygame.sprite.Sprite):
    """
    Generic superclass for all Sprites in the game. The
    constructor takes care of the setting up of sprites.
    """

    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)


class Weight(SquishSprite):
    """
    The class of the Weight sprite.
    """

    def __init__(self, speed):
        super().__init__(config.weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom


class Banana(SquishSprite):
    """
    The class of the Banana sprite.
    """

    def __init__(self):
        super().__init__(config.banana_image)
        self.rect.bottom = self.area.bottom

        self.pad_top = config.banana_pad_top
        self.pad_side = config.banana_pad_side

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)
