from __future__ import annotations

from direction import Direction
import random
from time import sleep

class Boarder:
    pass


class Game:
    def __init__(self, size: int = 4, start_tiles: int = 2):
        self.size = size
        self.tiles : list[list[int | None]] = [[None for x in range(size)] for y in range(size)]
        self.did_board_change = False
        self.game_over = False
        self.moves = 0
        self.score = 0

        for _ in range(start_tiles):
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

    # Movement
    def move(self, dir : Direction):
        self.did_board_change = False
        if dir == Direction.UP:
            for r in range(1, self.size):
                for c in range(self.size):
                    self.move_tile(r, c, dir)
        elif dir == Direction.DOWN:
            for r in range(self.size - 2, -1, -1):
                for c in range(self.size):
                    self.move_tile(r, c, dir)
        elif dir == Direction.LEFT:
            for c in range(1, self.size):
                for r in range(self.size):
                    self.move_tile(r, c, dir)
        elif dir == Direction.RIGHT:
            for c in range(self.size - 2, -1, -1):
                for r in range(self.size):
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
        self.tiles[x + dir.value[0]][y + dir.value[1]] *= 2
        self.score += self.tiles[x + dir.value[0]][y + dir.value[1]]
        self.tiles[x][y] = None
        self.did_board_change = True
        
    def create_tile(self, x: int, y: int, val) -> None:
        self.tiles[x][y] = val

    def create_random_tile(self):
        if self.is_board_full():
            return
        
        x = random.randint(0,self.size - 1)
        y = random.randint(0,self.size - 1)

        while not self.tiles[x][y] == None:
            x = random.randint(0,self.size - 1)
            y = random.randint(0,self.size - 1)

        self.create_tile(x, y, 2 if random.random() < 0.9 else  4)

    # Checks
    def can_move(self):
        for r in range(self.size):
            for c in range(self.size):
                val = self.tiles[r][c]
                if val == None:
                    return True
                if self.get_neigbor(r, c, Direction.RIGHT) == val or self.get_neigbor(r,c,Direction.DOWN) == val:
                    return True
                    
        return False
    
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


if(__name__ == "__main__"):
    g = Game(size=10)

    # i = ""
    # while not i == "q":
    #     g.__print__()
    #     # print(g.get_diffrence())
    #     print(f"Moves: {g.moves}")
    #     i = input()
    #     if i == 'r':
    #         g = Game()
    #     else:
    #         dir = Direction.to_dir(i)
    #         if not dir == None:
    #             g.move(dir)


    while True:
        try:
            
            g.move(Direction.UP)
            g.move(Direction.LEFT)
            g.move(Direction.DOWN)
            g.move(Direction.RIGHT)
            #print()
            #g.__print__()
            #sleep(.001)
        except:
            print("Game Over!\nFinal Board:")
            print(f"Moves: {g.moves}")
            g.__print__()
            break