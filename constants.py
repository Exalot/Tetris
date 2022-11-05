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
orange = (255, 127, 0)
purple = (127, 0, 127)
yellow = (255, 255, 0)
white = (255, 255, 255)
grey = (63, 63, 63)


def findLight(color: tuple[int, int, int]) -> tuple[int, int, int]:
    r1, g1, b1 = color
    r2, g2, b2 = white
    newR = int((r1 + r2) / 2)
    newG = int((g1 + g2) / 2)
    newB = int((b1 + b2) / 2)
    return newR, newG, newB


# Lighter versions of the colors to indicate their position after a hard drop
lightAqua = findLight(aqua)
lightBlue = findLight(blue)
lightGreen = findLight(green)
lightRed = findLight(red)
lightOrange = findLight(orange)
lightPurple = findLight(purple)
lightYellow = findLight(yellow)

# co-ordinates
x, y = 0, 1

# direction
DOWN = Vector2(0, 1)
RIGHT = Vector2(1, 0)
LEFT = Vector2(-1, 0)

# screen
tetrisDimensions = Vector2(10, 24)
blockSize = 40
screenSize = Vector2(tetrisDimensions.x * blockSize, tetrisDimensions.y * blockSize)

# Side Bar
sideBarSize = Vector2(200, screenSize.y)
# TODO: Maybe implemet top and bottom side bars too
whiteSquarePadding = Vector2(40, 75)

# Drop Time Management
startingDelayTime = 1.5
decreasePerSec = 1 / 45
lowestDelayTime = 0.5

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

"""        whiteSquare1 = pygame.Rect(constants.whiteSquarePadding.x, constants.whiteSquarePadding.y,
                                  constants.sideBarSize.x - 2 * constants.whiteSquarePadding.x,
                                  constants.sideBarSize.x - 2 * constants.whiteSquarePadding.x)"""
# TODO: Make the pieces a class and each one an object with attributes

#         rect2 = pygame.Rect(constants.sideBarSize.x + constants.screenSize.x, 0, constants.sideBarSize.x,
#                            constants.sideBarSize.y)

# pieces
I_PIECE = [[[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],

            [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]],

           [[Vector2(-2, 0), Vector2(-1, -1), Vector2(0, -2), Vector2(1, -3)],
            [Vector2(2, 0), Vector2(1, 1), Vector2(0, 2), Vector2(-1, 3)]],

           [pygame.Rect(whiteSquarePadding.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 0.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        4 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 0.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        4 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           aqua]

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
            [Vector2(1, 0), Vector2(1, 0), Vector2(-1, 1), Vector2(-1, 1)]],

           [pygame.Rect(whiteSquarePadding.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           blue]

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
            [Vector2(0, 0), Vector2(-1, 1), Vector2(-2, 2), Vector2(1, 1)]],

           [pygame.Rect(whiteSquarePadding.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           orange]

"""
L_PIECE_ROTATION = [[Vector2(2, 0), Vector2(0, 0), Vector2(-1, -1), Vector2(1, -2), Vector2(1, -2)],
           [Vector2(-2, 0), Vector2(2, -1), Vector2(1, 1), Vector2(-1, -1), Vector2(-1, -2)],
           [Vector2(0, 0), Vector2(0, 0), Vector2(-2, -1), Vector2(-2, -1), Vector2(1, -3)],
           [Vector2(1, 1), Vector2(0, 0), Vector2(-1, 2), Vector2(-2, 3), Vector2(2, 2)]]
"""

O_PIECE = [[[[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]]],

           [[Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]],

           [pygame.Rect(whiteSquarePadding.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           yellow]

"""O_PIECE_ROTATION = [Vector2(0, 0), Vector2(0, 0), Vector2(0, 0), Vector2(0, 0)]"""

S_PIECE = [[[[0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 5, 5, 0, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]],

           [[Vector2(0, 0), Vector2(0, 1), Vector2(2, 1), Vector2(0, 0)],
            [Vector2(0, 0), Vector2(0, -1), Vector2(-2, -1), Vector2(0, 0)]],

           [pygame.Rect(whiteSquarePadding.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           green]

"""S_PIECE_ROTATION = [[Vector2(0, 0), Vector2(0, -1), Vector2(2, 1), Vector2(0, 0)],
                    [Vector2(0, 0), Vector2(0, 0), Vector2(-2, 0), Vector2(0, -2)]]"""

Z_PIECE = [[[[0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 6, 0, 0, 0, 0]],

            [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 6, 0, 0, 0, 0],
             [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]],

           [[Vector2(2, 0), Vector2(0, 1), Vector2(1, 0), Vector2(-1, 1)],
            [Vector2(-2, 0), Vector2(0, -1), Vector2(-1, 0), Vector2(1, -1)]],

           [pygame.Rect(whiteSquarePadding.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           red]

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
            [Vector2(-1, 0), Vector2(0, -1), Vector2(0, -1), Vector2(0, -1)]],

           [pygame.Rect(whiteSquarePadding.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + screenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x))],
           purple]

# sideBarSize.x + screenSize.x

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
             -I_PIECE_INDEX: lightAqua,
             J_PIECE_INDEX: blue,
             -J_PIECE_INDEX: lightBlue,
             L_PIECE_INDEX: orange,
             -L_PIECE_INDEX: lightOrange,
             O_PIECE_INDEX: yellow,
             -O_PIECE_INDEX: lightYellow,
             S_PIECE_INDEX: green,
             -S_PIECE_INDEX: lightGreen,
             Z_PIECE_INDEX: red,
             -Z_PIECE_INDEX: lightRed,
             T_PIECE_INDEX: purple,
             -T_PIECE_INDEX: lightPurple}

pygame.font.init()

# text
"""co_ordinates = self.find_block_coordinates(Vector2(x, y))
                    rect = pygame.Rect(co_ordinates.x, co_ordinates.y, self.blockSize, self.
                                       blockSize)
                    pygame.draw.rect(self.screen, constants.colorDict[self.matrix[y][x]], rect)"""
score_font = pygame.font.SysFont("arial", 40)
score_font_shift = Vector2(275, 10)
side_bar_font = pygame.font.SysFont("arial", 32)
stored_piece_font_shift = Vector2(150, 30)
next_piece_font_shift = Vector2(20, 30)
end_font1 = pygame.font.SysFont("arial", 128)
end_font2 = pygame.font.SysFont("arial", 64)
game_over_text = "GAME OVER"
