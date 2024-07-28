import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, pos, num):
        super().__init__(groups)
        x = pos[0]
        y = pos[1]
        self.rect = pygame.Rect(x, y, 3, 20)
        self.direction = num
        sound = pygame.mixer.Sound('laser.mp3')
        sound.set_volume(0.1)
        sound.play()

    def update(self):
        pygame.draw.rect(pygame.display.get_surface(), 'red', self.rect)
        self.rect.centery += self.direction
        if self.rect.centery < 0 or self.rect.centery > 720:
            self.kill()
