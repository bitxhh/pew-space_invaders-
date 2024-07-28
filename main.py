import pygame
# from debug import debug
from level import Level
from settings import *
import sys


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height), vsync=1)
        self.clock = pygame.time.Clock()
        self.level = Level(self.display_surface)

        pygame.display.set_caption(title)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display_surface.fill('black')
            self.level.run()
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
