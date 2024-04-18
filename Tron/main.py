import pygame
from Settings import Settings
import Player
import math

game = Settings()

players = []


def setupPlayers():
    for p in range(2):
        keys = []
        key = None
        for k in range(4):
            selected = False
            while not selected:
                for e in pygame.event.get():
                    if e.type == pygame.KEYDOWN:
                        key = e.key
                        selected = True
            keys.append(key)
        players.append(Player.Player(p+1, game.PLAYER_COLORS[p], keys[3], keys[1], keys[0], keys[2]))


def tron():
    running = True
    game_start = False
    # game_pause = False
    game_over = False

    pygame.init()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit event
                running = False

            if event.type == pygame.KEYDOWN:  # keyboard events

                if event.key == pygame.K_ESCAPE:  # quit on esc
                    running = False

                if event.key == pygame.K_RETURN and not game_start:
                    game_start = True
                    print("let the games begin")

                for player in range(2):
                    players[player].setDirection(event)

        if not game_start:

            mouse_left, mouse_mid, mouse_right = pygame.mouse.get_pressed()
            mouse_pos = getPosOnGrid()  # get button clicked and position

            if mouse_left:  # set player_one start pos
                players[0].pos = mouse_pos
                game.grid[mouse_pos] = players[0].num

            if mouse_right:  # set player_two start pos
                players[1].pos = mouse_pos
                game.grid[mouse_pos] = players[1].num

            if mouse_mid:  # erase player pos
                for player in range(2):
                    if game.grid[mouse_pos] != 0:
                        players[int(game.grid[mouse_pos])-1].pos = None
                        game.grid[mouse_pos] = 0

        elif game_over:
            # game over code goes here
            print("game over")
            pygame.font.Font("")
            running = False

        elif game_start:

            try:
                for player in range(2):
                    position, player_number = players[player].movePlayer(game.grid)
                    game.grid[position] = player_number
            except TypeError:
                game_over = True

        drawGrid()
        pygame.display.update()


def getPosOnGrid():
    x, y = pygame.mouse.get_pos()

    pos_x = math.floor(x / game.block_width)
    pos_y = math.floor(y / game.block_height)

    return pos_x, pos_y


def drawGrid():
    for x, row in enumerate(game.grid):
        for y, pos in enumerate(row):
            block = pygame.Rect((x * game.block_width), (y * game.block_height), game.block_width, game.block_height)

            for player in range(2):
                if pos == players[player].num:
                    pygame.draw.rect(game.window, players[player].color, block)


if __name__ == "__main__":
    tron()
