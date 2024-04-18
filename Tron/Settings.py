import pygame
import numpy


class Settings:
    def __init__(self):
        # COLORS
        self.BLACK = (10, 10, 10)
        self.PLAYER_COLORS = [
            (166, 46, 180),  # PURPLE
            (46, 166, 180),  # BLUE
            (255, 47, 180),  # PINK
            (255, 255, 180)  # CREME
        ]

        # RESOLUTION/SCALE
        self.screen_res = (1600, 900)
        self.block_width, self.block_height = 10, 10
        self.blocks_x = int(self.screen_res[0] / self.block_width)
        self.blocks_y = int(self.screen_res[1] / self.block_height)

        # WINDOW/GRID INITIALIZATION
        self.window = pygame.display.set_mode(self.screen_res)
        self.window.fill(self.BLACK)
        self.grid = numpy.zeros((self.blocks_x, self.blocks_y))
