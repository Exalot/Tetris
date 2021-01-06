"""
Constant values
"""

import pygame

debugMode = True

# colors
black = (0, 0, 0)
aqua = (0, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 128, 0)
purple = (128, 0, 128)
yellow = (255, 255, 0)
white = (255, 255, 255)

# co-ordinates
x, y = 0, 1

# direction
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

# pieces
I_PIECE = [[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],

           [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]]

J_PIECE = [[[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 0, 0, 0, 0, 0]],

           [[0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]],

           [[0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0]],

           [[0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0]]]

L_PIECE = [[[0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 3, 0, 0, 0, 0]],

           [[0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 3, 3, 3, 0, 0, 0]],

           [[0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]],

           [[0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 0, 0, 0, 0]]]

O_PIECE = [[[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]]]

S_PIECE = [[[0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 5, 5, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]]

Z_PIECE = [[[0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 6, 0, 0, 0, 0]],

           [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 6, 0, 0, 0, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]]

T_PIECE = [[[0, 0, 0, 7, 7, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]],

           [[0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 7, 0, 0, 0, 0]],

           [[0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 0, 7, 7, 7, 0, 0, 0, 0]],

           [[0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 7, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]]]


def get_pieces():
    """
    A function for returning a deep copy of all tetris piece blueprints
    :return:
    """
    return [I_PIECE, J_PIECE, L_PIECE, O_PIECE, S_PIECE, Z_PIECE, T_PIECE]


# indexes
I_PIECE_INDEX, J_PIECE_INDEX, L_PIECE_INDEX, O_PIECE_INDEX, S_PIECE_INDEX, Z_PIECE_INDEX, T_PIECE_INDEX = range(1, 8)

# color dictionary
colorDict = {I_PIECE_INDEX: aqua,
             J_PIECE_INDEX: blue,
             L_PIECE_INDEX: orange,
             O_PIECE_INDEX: yellow,
             S_PIECE_INDEX: green,
             Z_PIECE_INDEX: red,
             T_PIECE_INDEX: purple}

pygame.font.init()

# text
score_font = pygame.font.SysFont("arial", 24)
score_font_shift = (-250, 5)
end_font1 = pygame.font.SysFont("arial", 128)
end_font2 = pygame.font.SysFont("arial", 64)
game_over_text = "GAME OVER"

