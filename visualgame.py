from __future__ import annotations
from fastgame import Game
from fastgame import Direction
import pygame

game = Game(size=6)

pygame.init()

tileSize = 100
boardSize = 20
top_size = 40

x_size = game.size*(tileSize+boardSize) + boardSize
y_size = game.size*(tileSize+boardSize) + boardSize + top_size

screen = pygame.display.set_mode([x_size, y_size])
pygame.display.set_caption("2048")

font=pygame.font.SysFont('timesnewroman',  30)


def draw_board():
    for x in range(game.size):
        for y in range(game.size):
            x_pos = boardSize + y*(tileSize+boardSize)
            y_pos = boardSize + x*(tileSize+boardSize) + top_size
            val = game.tiles[x][y]

            text = font.render(f"Moves: {game.moves}", True, (255, 255, 255))
            screen.blit(text, (10, 10))

            text = font.render(f"Score: {game.score}", True, (255, 255, 255))
            screen.blit(text, (300, 10))

            if(val == None):
                color = (90, 90, 90)
                pygame.draw.rect(screen, color, [x_pos, y_pos, tileSize, tileSize])
            else:
                color = (50, 50, 50)
                pygame.draw.rect(screen, color, [x_pos, y_pos, tileSize, tileSize])
                text = font.render(str(val), True, (255, 255, 255))
                screen.blit(text, (x_pos + tileSize/2 - text.get_width()/2, y_pos + tileSize/2 - text.get_height()/2))  


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.move(Direction.UP)
            if event.key == pygame.K_s:
                game.move(Direction.DOWN)
            if event.key == pygame.K_a:
                game.move(Direction.LEFT)
            if event.key == pygame.K_d:
                game.move(Direction.RIGHT)

    screen.fill((33, 33, 33))
    draw_board()

    if(game.game_over):
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (x_size/2, y_size/2))

    pygame.display.update()


pygame.quit()