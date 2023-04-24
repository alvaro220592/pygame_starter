# Arquivo principal do projeto
import pygame
import constants
from classes.object import Object


class Main:
    def __init__(self, window_x, window_y, title):
        self.window = pygame.display.set_mode((window_x, window_y))
        pygame.display.set_caption(title)

        self.loop = True

    def draw(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

game = Main(constants.WINDOW['WIDTH'], constants.WINDOW['HEIGHT'], constants.GAME_TITLE)
game.update()
