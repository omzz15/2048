from __future__ import annotations
from gamecore import GameCore
from gamecore import Direction
import pygame

class GameVisulizerSettings:
    def __init__(self, tileSize: int = 100, boardSize: int = 20, top_size: int= 40, font_name : str = 'timesnewroman'):
        self.tileSize = tileSize
        self.boardSize = boardSize
        self.top_size = top_size
        self.font_name = font_name

class GameVisulizer:
    settings : GameVisulizerSettings = GameVisulizerSettings()
    pygame.display.set_caption("2048")

    @classmethod
    def draw_board(cls):
        cls.screen.fill((33, 33, 33))
        for x in range(cls.game.size):
            for y in range(cls.game.size):
                x_pos = cls.settings.boardSize + y*(cls.settings.tileSize+cls.settings.boardSize)
                y_pos = cls.settings.boardSize + x*(cls.settings.tileSize+cls.settings.boardSize) + cls.settings.top_size
                val = cls.game.tiles[x][y]

                text = cls.font.render(f"Moves: {cls.game.moves}", True, (255, 255, 255))
                cls.screen.blit(text, (10, 10))

                text = cls.font.render(f"Score: {cls.game.score}", True, (255, 255, 255))
                cls.screen.blit(text, (300, 10))

                if(val == None):
                    color = (90, 90, 90)
                    pygame.draw.rect(cls.screen, color, [x_pos, y_pos, cls.settings.tileSize, cls.settings.tileSize])
                else:
                    color = (50, 50, 50)
                    pygame.draw.rect(cls.screen, color, [x_pos, y_pos, cls.settings.tileSize, cls.settings.tileSize])
                    text = cls.font.render(str(val), True, (255, 255, 255))
                    cls.screen.blit(text, (x_pos + cls.settings.tileSize/2 - text.get_width()/2, y_pos + cls.settings.tileSize/2 - text.get_height()/2))  
        if(cls.game.game_over):
            text = cls.font.render("Game Over", True, (255, 255, 255))
            cls.screen.blit(text, (cls.x_size/2, cls.y_size/2))
        
        pygame.display.update()

    @classmethod
    def start(cls, game: GameCore):
        cls.game = game
        
        cls.x_size = game.size*(cls.settings.tileSize+cls.settings.boardSize) + cls.settings.boardSize
        cls.y_size = game.size*(cls.settings.tileSize+cls.settings.boardSize) + cls.settings.boardSize + cls.settings.top_size

        cls.screen = pygame.display.set_mode([cls.x_size, cls.y_size])

        cls.font = pygame.font.SysFont(cls.settings.font_name, 30)

pygame.init()
gc = GameCore()

GameVisulizer.start(gc)
GameVisulizer.draw_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                gc.move(Direction.UP)
            if event.key == pygame.K_s:
                gc.move(Direction.DOWN)
            if event.key == pygame.K_a:
                gc.move(Direction.LEFT)
            if event.key == pygame.K_d:
                gc.move(Direction.RIGHT)
            
            GameVisulizer.draw_board()

pygame.display.quit()
pygame.quit()