import pygame
from entity import Entity
from random import randint
from bullet import Bullet


class Enemy(Entity):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.name = 'enemy'
        self.image = pygame.image.load('tile023.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.move_time = pygame.time.get_ticks()

    def do_shoot(self):
        if pygame.time.get_ticks() - self.shoot_time > randint(2000, 20000):
            Bullet(self.alien_bullet_group, self.rect.midbottom + pygame.math.Vector2(0, 10), 5)
            self.shoot_time = pygame.time.get_ticks()

    def update(self, direction):
        if pygame.time.get_ticks() - self.move_time > 60:
            self.move(self.speed, direction)
            self.move_time = pygame.time.get_ticks()
