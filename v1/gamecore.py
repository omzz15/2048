from __future__ import annotations

from direction import Direction
import random

class Boarder:
    pass

class GameCore:
    def __init__(self, x_size: int = 4, y_size: int = 4, start_tiles: int = 2):
        self.start_tiles = start_tiles
        self.x_size = x_size
        self.y_size = y_size
        self.reset()

    def reset(self) -> None: 
        self.tiles : list[list[int | None]] = [[None for x in range(self.x_size)] for y in range(self.y_size)]
        self.did_board_change = False
        self.game_over = False
        self.moves = 0
        self.score = 0
        self.largest_tile = 0

        for _ in range(self.start_tiles):
            self.create_random_tile()

    def get_neigbor(self, x: int, y: int, dir : Direction) -> int | Boarder:
        try:
            return self.tiles[x + dir.value[0]][y + dir.value[1]]
        except:
            return Boarder

    def is_board_full(self):
        for r in self.tiles:
            for c in r:
                if c == None:
                    return False
        return True

    # Movementsize
    def move(self, dir : Direction):
        self.did_board_change = False
        if self.y_size > 1:
            if dir == Direction.UP:
                for r in range(1, self.y_size):
                    for c in range(self.x_size):
                        self.move_tile(r, c, dir)
            elif dir == Direction.DOWN:
                for r in range(self.y_size - 2, -1, -1):
                    for c in range(self.x_size):
                        self.move_tile(r, c, dir)
        
        if self.x_size > 1:
            if dir == Direction.LEFT:
                for c in range(1, self.x_size):
                    for r in range(self.y_size):
                        self.move_tile(r, c, dir)
            elif dir == Direction.RIGHT:
                for c in range(self.x_size - 2, -1, -1):
                    for r in range(self.y_size):
                        self.move_tile(r, c, dir)
        
        
        if self.did_board_change:
            self.create_random_tile()
            self.moves += 1
        if not self.can_move():
            self.game_over = True

    def move_tile(self, x, y, dir : Direction):
        if(self.tiles[x][y] == None):
            return

        curr_x, curr_y = x, y
        n = self.get_neigbor(curr_x, curr_y, dir)
        
        while n == None:
            curr_x, curr_y = self.move_one_space(curr_x, curr_y, dir)
            n = self.get_neigbor(curr_x, curr_y, dir)
        
        if n == self.tiles[curr_x][curr_y]:
            self.merge(curr_x, curr_y, dir)

    def move_one_space(self, x, y, dir: Direction):
        new_x, new_y = x + dir.value[0], y + dir.value[1]
        self.tiles[new_x][new_y] = self.tiles[x][y]
        self.tiles[x][y] = None
        self.did_board_change = True
        return new_x, new_y

    # tile editing
    def merge(self, x, y, dir: Direction):
        val = self.tiles[x + dir.value[0]][y + dir.value[1]] * 2
        self.tiles[x + dir.value[0]][y + dir.value[1]] = val
        
        if(val > self.largest_tile): self.largest_tile = val
        self.score += val
        self.tiles[x][y] = None
        self.did_board_change = True
        
    def create_tile(self, x: int, y: int, val) -> None:
        self.tiles[x][y] = val

    def create_random_tile(self):
        if self.is_board_full():
            return
        
        x = random.randint(0,self.y_size - 1)
        y = random.randint(0,self.x_size - 1)

        while not self.tiles[x][y] == None:
            x = random.randint(0,self.y_size - 1)
            y = random.randint(0,self.x_size - 1)

        self.create_tile(x, y, 2 if random.random() < 0.9 else  4)

    # Checks
    def can_move(self):
        for r in range(self.y_size):
            for c in range(self.x_size):
                val = self.tiles[r][c]
                if val == None:
                    return True
                if self.get_neigbor(r, c, Direction.RIGHT) == val or self.get_neigbor(r,c,Direction.DOWN) == val:
                    return True
                    
        return False

    #Misc
    def __print__(self):
        for r in self.tiles:
            out = ""
            for c in r:    
                if(c == None):
                    out += "-\t"
                else:
                    out += str(c) + "\t"
                out += " "
            print(out)
            print()
            print()