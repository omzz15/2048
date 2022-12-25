from enum import Enum

class Direction(Enum):
    UP = (-1,0)
    DOWN = (1,0)
    LEFT = (0,-1)
    RIGHT = (0, 1)

    
    def to_dir(input : str):
        if input == 'w':
            return Direction.UP
        elif input == 's':
            return Direction.DOWN
        elif input == 'a':
            return Direction.LEFT
        elif input == 'd':
            return Direction.RIGHT