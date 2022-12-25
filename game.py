# from direction import Direction
# from tile import Tile
# from time import sleep

# import random

# class Game:
#     def __init__(self, size: int = 4, start_tiles: int = 2):
#         self.size = size
#         self.tiles : list[list[Tile]] = [[None for x in range(size)] for y in range(size)]
#         self.did_board_change = False
#         self.moves = 0
#         self.create_random_tile()
#         self.create_random_tile()

#     def move_game(self, dir: Direction):
#         self.pre_move()
#         if dir == Direction.UP:
#             self.move_up()
#         elif dir == Direction.DOWN:
#             self.move_down()
#         elif dir == Direction.LEFT:
#             self.move_left()
#         elif dir == Direction.RIGHT:
#             self.move_right()
#         self.post_move()

#     def pre_move(self):
#         self.did_board_change = False

#     def post_move(self):
#         if self.did_board_change:
#             self.create_random_tile()
#             self.moves += 1
#         if not self.can_move():
#             raise Exception("game over")

#     def move_up(self):
#         for r in range(1, self.size):
#             for c in range(self.size):
#                 tile = self.tiles[r][c]
#                 if not tile == None: tile.move(Direction.UP)

#     def move_down(self):
#         for r in range(self.size - 2, -1, -1):
#             for c in range(self.size):
#                 tile = self.tiles[r][c]
#                 if not tile == None: tile.move(Direction.DOWN)
    
#     def move_left(self):
#         for c in range(1, self.size):
#             for r in range(self.size):
#                 tile = self.tiles[r][c]
#                 if not tile == None: tile.move(Direction.LEFT)
    
#     def move_right(self):
#         for c in range(self.size - 2, -1, -1):
#             for r in range(self.size):
#                 tile = self.tiles[r][c]
#                 if not tile == None: tile.move(Direction.RIGHT)

#     def move_tile(self, tile: Tile, x: int, y: int) -> None:
#         self.tiles[tile.x][tile.y] = None
#         tile.x = x
#         tile.y = y
#         self.tiles[x][y] = tile
#         self.did_board_change = True

#     def move_tile_dir(self, tile: Tile, dir : Direction):
#         self.move_tile(tile, tile.x + dir.value[0], tile.y + dir.value[1])

#     def create_tile(self, x: int, y: int, val = 0) -> None:
#         self.tiles[x][y] = Tile(self, x, y, val)

#     def is_board_full(self):
#         for r in self.tiles:
#             for c in r:
#                 if c == None:
#                     return False
#         return True

#     def create_random_tile(self):
#         if self.is_board_full():
#             return
        
#         x = random.randint(0,self.size - 1)
#         y = random.randint(0,self.size - 1)

#         while not self.tiles[x][y] == None:
#             x = random.randint(0,self.size - 1)
#             y = random.randint(0,self.size - 1)

#         self.create_tile(x, y, 2 if random.random() < 0.9 else  4)

#     def delete_tile(self, x: int, y: int) -> None:
#         self.tiles[x][y] = None
#         self.did_board_change = True

#     def can_move(self):
#         for r in self.tiles:
#             for c in r:
#                 if (not c == None) and c.is_valid_move_avalible():
#                     return True
#         return False

#     def get_value(self, r:int, c:int):
#         t = self.tiles[r][c]
#         return t.val if not t == None else 0

#     def get_diffrence(self):
#         diff_col : list[list] = []
#         diff_row : list[list] = []
#         for r in range(self.size):
#             diff_col.append([])
#             if not r == self.size - 1:
#                 diff_row.append([])
#             for c in range(self.size):
#                 if not r == self.size - 1:
#                     diff_row[r].append(abs(self.get_value(r, c) - self.get_value(r + 1,c)))
#                 if not c == self.size - 1:
#                     diff_col[r].append(abs(self.get_value(r, c) - self.get_value(r, c + 1)))
#         return(diff_row, diff_col)

#     def __print__(self):
#         for r in self.tiles:
#             out = ""
#             for c in r:    
#                 if(c == None):
#                     out += "-\t"
#                 else:
#                     out += str(c.val) + "\t"
#                 out += " "
#             print(out)
#             print()
#             print()


# g = Game(size=8)
# # i = ""
# # while not i == "q":
# #     g.__print__()
# #     # print(g.get_diffrence())
# #     print(f"Moves: {g.moves}")
# #     i = input()
# #     if i == 'r':
# #         g = Game()
# #     else:
# #         dir = Direction.to_dir(i)
# #         if not dir == None:
# #             g.move_game(dir)


# # #print(t.values[3][3].getNeigbor(Direction.UP))

# # while True:
# #     i = random.random()
# #     if(i < 0.25):
# #         g.move_game(Direction.UP)
# #     elif(i < 0.5):
# #         g.move_game(Direction.DOWN)
# #     elif(i < 0.75):
# #         g.move_game(Direction.LEFT)
# #     else:
# #         g.move_game(Direction.RIGHT)
# #     print()
# #     g.__print__()
# #     sleep(.5)

# #print 50 to 700
