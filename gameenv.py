import random
from time import sleep

import pygame
from direction import Direction

from gamecore import GameCore
from visualgame import GameVisulizer

class GameEnviornment(GameCore):
    def __init__(self, size: int = 4, start_tiles: int = 2, render = True):
        super().__init__(size, start_tiles)
        
        if(render):
            pygame.init()
            GameVisulizer.start(self)

    def reset(self) -> list[int]:
        super().reset()
        return self.get_state()

    def get_sample_move(self) -> int:
        return random.randint(0,3)

    def get_state(self) -> list[int]:
        return [(item if not item == None else 0) for sublist in self.tiles for item in sublist]

    def step(self, move) -> tuple[list[int], int, bool]:
        start_score = self.score
        self.move(Direction.to_dir_from_num(move))
        return (self.get_state(), self.score, self.game_over or self.largest_tile >= 2048)

    def render(self):
        GameVisulizer.draw_board()

    def stop_render(self):
        pygame.display.quit()

    def close(self):
        GameVisulizer.close()
        pygame.quit()