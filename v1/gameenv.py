import random

import pygame
from direction import Direction

from gamecore import GameCore
from visualgame import GameVisulizer

class GameEnviornment(GameCore):
    def __init__(self, x_size : int = 4, y_size : int = 4, start_tiles: int = 2, render = True):
        super().__init__(x_size, y_size, start_tiles)
        
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
        open_tiles = self.get_num_of_open_tiles()
        start_score = self.score
        last_high = self.largest_tile

        self.move(Direction.to_dir_from_num(move))

        return (self.get_state(), self.get_reward(start_score, last_high, open_tiles), self.game_over or self.largest_tile >= 2048)

    def get_reward(self, start_score, last_high, open_tiles) -> int:
        return self.score - start_score + (self.largest_tile - last_high) * 4 - (1000 if self.game_over else 0) - 10 if not self.did_board_change else 0 + 50 * (self.get_num_of_open_tiles() - open_tiles)

    def get_num_of_open_tiles(self) -> int:
        return sum([1 for sublist in self.tiles for item in sublist if item == None])

    def render(self):
        GameVisulizer.draw_board()

    def stop_render(self):
        pygame.display.quit()

    def close(self):
        GameVisulizer.close()
        pygame.quit()