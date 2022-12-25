# from __future__ import annotations

# from direction import Direction

# if not 1 == 1:
#     from game import Game

# class Tile:
#     def __init__(self, game : Game, x : int, y : int, val : int = 0):
#         self.game = game
#         self.x = x
#         self.y = y
#         self.val = val  

#     def get_neigbor(self, dir : Direction) -> Tile | Boarder:
#         try:
#             return self.game.tiles[self.x + dir.value[0]][self.y + dir.value[1]]
#         except:
#             return Boarder

#     def is_valid_move(self, dir : Direction):
#         neighbor = self.get_neigbor(dir)

#         if neighbor == Boarder:
#             return False

#         if neighbor == None or neighbor.val == self.val:
#             return True

#         return False

#     def is_valid_move_avalible(self):
#         for dir in Direction:
#             if self.is_valid_move(dir): return True
#         return False

#     def move(self, dir : Direction):
#         neighbor = self.get_neigbor(dir)

#         while neighbor == None:
#             self.game.move_tile_dir(self, dir)
#             neighbor = self.get_neigbor(dir)
            
#         if not neighbor == Boarder and neighbor.val == self.val:
#             neighbor.val *= 2
#             self.game.delete_tile(self.x, self.y)

# class Boarder:
#     pass
