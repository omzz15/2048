from enum import Enum

class Direction(Enum):
    UP = (-1,0)
    DOWN = (1,0)
    LEFT = (0,-1)
    RIGHT = (0, 1)

    
    def to_dir_from_str(input : str):
        if input == 'w':
            return Direction.UP
        elif input == 's':
            return Direction.DOWN
        elif input == 'a':
            return Direction.LEFT
        elif input == 'd':
            return Direction.RIGHT
    
    def to_dir_from_num(input: int):
        if input == 0:
            return Direction.UP
        elif input == 1:
            return Direction.DOWN
        elif input == 2:
            return Direction.LEFT
        elif input == 3:
            return Direction.RIGHT