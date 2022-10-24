"""
Constant values
"""

import pygame
from vector2 import Vector2

debugMode = True

zeroVector = Vector2(0, 0)

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
DOWN = Vector2(0, 1)
RIGHT = Vector2(1, 0)
LEFT = Vector2(-1, 0)

# TODO: https://prnt.sc/bvCqMQiGrpWC blue rotation from last to normal
#       https://prnt.sc/jiPU4hdiGfPH first green rotation DONE
#       https://prnt.sc/t_Ic9NnBpoQh second red rotation DONE
#       https://prnt.sc/bafic80fwxUb second orange rotation
#       https://prnt.sc/fUhpTfln9qFm, https://prnt.sc/TooetMe_uv4A
#       SQUARE JUST GIVES ERRORS
#       https://prnt.sc/bSX4GKUfJ7D8 second purple rotation
#
# https://prnt.sc/dUGQkKfvfOgE, https://prnt.sc/26KYLrEDKbAX

"""I_PIECE_ROTATION = [[Vector2(-2, 0), Vector2(-1, -1), Vector2(0, -2), Vector2(1, -3)],
                    Vector2(2, 0), Vector2(1, 1), Vector2(0, 2), Vector2(-1, 3)]"""

# pieces
I_PIECE = [[[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],

            [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]],

           [[Vector2(-2, 0), Vector2(-1, -1), Vector2(0, -2), Vector2(1, -3)],
           [Vector2(2, 0), Vector2(1, 1), Vector2(0, 2), Vector2(-1, 3)]]]

J_PIECE = [[[[0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 2, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 2, 2, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]],

            [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 2, 2, 2, 0, 0, 0]]],

           [[Vector2(-1, 0), Vector2(0, -1), Vector2(2, -2), Vector2(1, -1)],
            [Vector2(0, 0), Vector2(0, 0), Vector2(-2, 1), Vector2(-2, 1)],
            [Vector2(0, 0), Vector2(-1, 1), Vector2(1, 0), Vector2(2, -1)],
            [Vector2(1, 0), Vector2(1, 0), Vector2(-1, 1), Vector2(-1, 1)]]]

"""
J_PIECE_ROTATION = [[Vector2(-2, 0), Vector2(-1, -1), Vector2(0, -2), Vector2(2, -3), Vector2(1, -2)],
                    [Vector2(1, 1), Vector2(0, 0), Vector2(0, 0), Vector2(-2, 2), Vector2(-2, 2)],
                    [Vector2(-1, 0), Vector2(-2, 1), Vector2(0, 0), Vector2(1, -1), Vector2(2, -2)],
                    [Vector2(2, 0), Vector2(2, 1), Vector2(1, 2), Vector2(0, 0), Vector2(-2, 2)]]
                    """

L_PIECE = [[[[0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 3, 3, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
             [0, 0, 0, 0, 3, 3, 3, 0, 0, 0]],

            [[0, 0, 0, 0, 3, 3, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 3, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
             [0, 0, 0, 0, 3, 0, 0, 0, 0, 0]]],

           [[Vector2(2, 0), Vector2(0, 0), Vector2(1, -1), Vector2(1, -1)],
            [Vector2(-2, 0), Vector2(1, -1), Vector2(0, 0), Vector2(-1, 1)],
            [Vector2(0, 0), Vector2(0, 0), Vector2(1, -1), Vector2(-1, -1)],
            [Vector2(0, 0), Vector2(-1, 1), Vector2(-2, 2), Vector2(1, 1)]]]

"""
L_PIECE_ROTATION = [[Vector2(2, 0), Vector2(0, 0), Vector2(-1, -1), Vector2(1, -2), Vector2(1, -2)],
           [Vector2(-2, 0), Vector2(2, -1), Vector2(1, 1), Vector2(-1, -1), Vector2(-1, -2)],
           [Vector2(0, 0), Vector2(0, 0), Vector2(-2, -1), Vector2(-2, -1), Vector2(1, -3)],
           [Vector2(1, 1), Vector2(0, 0), Vector2(-1, 2), Vector2(-2, 3), Vector2(2, 2)]]
"""

O_PIECE = [[[[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]]],

           [[Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]]]

"""O_PIECE_ROTATION = [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]"""

S_PIECE = [[[[0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 5, 5, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]],

           [[Vector2(0, 0), Vector2(0, 1), Vector2(2, 1), Vector2(0, 0)],
            [Vector2(0, 0), Vector2(0, -1), Vector2(-2, -1), Vector2(0, 0)]]]

"""S_PIECE_ROTATION = [[Vector2(0, 0), Vector2(0, -1), Vector2(2, 1), Vector2(0, 0)],
                    [Vector2(0, 0), Vector2(0, 0), Vector2(-2, 0), Vector2(0, -2)]]"""

Z_PIECE = [[[[0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 6, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 6, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]],

           [[Vector2(2, 0), Vector2(0, 1), Vector2(1, 0), Vector2(-1, 1)],
            [Vector2(-2, 0), Vector2(0, -1), Vector2(-1, 0), Vector2(1, -1)]]]

"""Z_PIECE_ROTATION = [[Vector2(2, 0), Vector2(0, 2), Vector2(0, 0), Vector2(0, 0)],
                    [Vector2(-2, 0), Vector2(0, 0), Vector2(0, 0), Vector2(0, -2)]]"""

T_PIECE = [[[[0, 0, 0, 7, 7, 7, 0, 0, 0, 0],
             [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
             [0, 0, 0, 0, 7, 7, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 7, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 7, 7, 7, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 7, 7, 0, 0, 0, 0],
             [0, 0, 0, 0, 7, 0, 0, 0, 0, 0]]],

           [[Vector2(2, 0), Vector2(0, 1), Vector2(0, 1), Vector2(1, 1)],
            [Vector2(-1, 0), Vector2(-1, 0), Vector2(-1, 0), Vector2(0, -1)],
            [Vector2(0, 0), Vector2(1, 0), Vector2(1, 0), Vector2(-1, 1)],
            [Vector2(-1, 0), Vector2(0, -1), Vector2(0, -1), Vector2(0, -1)]]]

"""T_PIECE_ROTATION = [[Vector2(2, 1), Vector2(1, 2), Vector2(0, 0), Vector2(0, 0)],
                    [Vector2(-1, 0), Vector2(0, 0), Vector2(0, 0), Vector2(-2, -1)],
                    [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), Vector2(-1, -1)]]"""

# rotation vectors


def get_pieces():
    """
    A function for returning a deep copy of all tetris piece blueprints
    :return: a list of pieces
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
score_font_shift = Vector2(-250, 5)
end_font1 = pygame.font.SysFont("arial", 128)
end_font2 = pygame.font.SysFont("arial", 64)
game_over_text = "GAME OVER"
