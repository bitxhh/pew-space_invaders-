import pygame
from bullet import Bullet


class Entity(pygame.sprite.Sprite):
    bullet_group = pygame.sprite.Group()
    alien_bullet_group = pygame.sprite.Group()

    def __init__(self, groups):
        super().__init__(groups)
        self.direction = 0
        self.shoot_time = pygame.time.get_ticks()

    def move(self, speed, direction):
        if direction > 0:
            self.rect.x += speed
        if direction < 0:
            self.rect.x -= speed
