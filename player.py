import pygame
from settings import *
from entity import Entity
from bullet import Bullet
from debug import debug


class Player(Entity):
    def __init__(self, groups, reset):
        super().__init__(groups)
        self.name = 'player'
        self.reset = reset
        self.image = pygame.image.load('tile041.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(window_width // 2, 690))
        self.speed = 5
        self.Alive = True
        self.score = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = -1
        elif keys[pygame.K_d]:
            self.direction = 1
        else:
            self.direction = 0
        if keys[pygame.K_SPACE]:
            if pygame.time.get_ticks() - self.shoot_time > 450:
                Bullet(self.bullet_group, self.rect.midtop + pygame.math.Vector2(0, -20), -3)
                self.shoot_time = pygame.time.get_ticks()

    def collision(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= window_width:
            self.rect.right = window_width

    def check_death(self):
        if not self.Alive:
            text_surf = pygame.font.Font(UI_FONT, 40).render('You dead', True, TEXT_COLOR)
            text_surf2 = pygame.font.Font(UI_FONT, 20).render('Enter to restart', False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(window_width // 2, window_height // 2))
            text_rect2 = text_surf2.get_rect(center=(window_width // 2, window_height // 2 + 30))
            pygame.display.get_surface().blit(text_surf, text_rect)
            pygame.display.get_surface().blit(text_surf2, text_rect2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.reset()

    def update(self, direction):
        self.input()
        self.move(self.speed, self.direction)
        self.collision()
        self.check_death()
        debug(self.score)
