import pygame
from settings import *
from Enemy import Enemy
from player import Player
from entity import Entity
from random import choice


class Level:
    def __init__(self, displey_surface):
        self.displey_surface = displey_surface
        self.entity_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.spawn_enemy()
        self.enemy_direction = 1
        self.cross_time = pygame.time.get_ticks()
        self.music = pygame.mixer.Sound('music.mp3')
        self.music.set_volume(0.2)
        self.music.play(loops=-1)
        self.success = pygame.mixer.Sound('success.wav')
        self.dead_sfx = pygame.mixer.Sound('dead.wav')

    def spawn_enemy(self):
        for i in range(17):
            for k in range(4):
                Enemy([self.entity_group, self.enemy_group], (32 * i + 1, 32 * k))
        self.player = Player(self.entity_group, self.reset)

    def downing_enemy(self):
        for sprite in self.entity_group:
            if sprite.name == 'enemy':
                sprite.rect.y += 32

    def check_across(self):
        for sprite in self.enemy_group:
            if pygame.time.get_ticks() - self.cross_time > 200:
                if sprite.rect.right >= window_width:
                    self.enemy_direction = -1
                    self.downing_enemy()
                    self.cross_time = pygame.time.get_ticks()
                elif sprite.rect.left <= 0:
                    self.enemy_direction = 1
                    self.downing_enemy()
                    self.cross_time = pygame.time.get_ticks()
            if sprite.rect.bottom >= 680:
                self.player.Alive = False

    def check_death(self):
        if Entity.bullet_group:
            for sprite in Entity.bullet_group:
                if pygame.sprite.spritecollide(sprite, self.enemy_group, True):
                    self.player.score += 100
                    sprite.kill()
        if Entity.alien_bullet_group:
            if pygame.sprite.spritecollide(self.player, Entity.alien_bullet_group, True):
                self.player.Alive = False
                self.dead_sfx.play()
                self.player.kill()

    def reset(self):
        for sprite in self.entity_group:
            sprite.kill()
        for sprite in self.enemy_group:
            sprite.kill()
        for sprite in Entity.bullet_group:
            sprite.kill()
        for sprite in Entity.alien_bullet_group:
            sprite.kill()
        del self.player
        self.spawn_enemy()

    def check_enemy_exists(self):
        if self.enemy_group:
            choice(self.enemy_group.sprites()).do_shoot()
        else:
            for sprites in Entity.alien_bullet_group:
                sprites.kill()
            self.success.play()
            text_surf = pygame.font.Font(UI_FONT, 40).render('You win', True, TEXT_COLOR)
            text_surf2 = pygame.font.Font(UI_FONT, 20).render('Enter to restart', False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(window_width // 2, window_height // 2))
            text_rect2 = text_surf2.get_rect(center=(window_width // 2, window_height // 2 + 30))
            pygame.display.get_surface().blit(text_surf, text_rect)
            pygame.display.get_surface().blit(text_surf2, text_rect2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.reset()

    def run(self):
        self.entity_group.draw(self.displey_surface)
        if self.player.Alive:
            self.check_enemy_exists()
            self.entity_group.update(self.enemy_direction)
            Entity.bullet_group.update()
            Entity.alien_bullet_group.update()
            self.check_across()
            self.check_death()
        else:
            self.player.update(0)
