"""
Constant values
"""

import pygame
from vector2 import Vector2

debugMode = True

zeroVector = Vector2(0, 0)

# Game States
mainMenu, scores, inGame, pausedGame, gameOver = range(0, 5)

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
dark_grey = (23, 23, 23)
light_grey = (191, 191, 191)

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

# Main Menu Buttons
menuPlayButtonOffset = Vector2(150, 300)
endGameButtonOffset = Vector2(200, 0)
menuPlayButtonTextPos = Vector2(315, 280)

menuScoresButtonOffset = Vector2(150, 500)
menuScoresButtonTextPos = Vector2(275, 480)

menuQuitButtonOffset = Vector2(150, 700)
menuQuitButtonTextPos = Vector2(315, 680)

# Paused Game Buttons

 # endGameButtonSize = Vector2(fullScreenSize.x - endGameButtonOffset.x * 2, 100)

pausedPlatformOffsetTop = Vector2(120, 200)

pausedContinueButtonOffset = Vector2(200, 250)
pausedContinueButtonTextPos = Vector2(275, 250)

pausedMenuButtonOffset = Vector2(200, 400)
pausedMenuButtonTextPos = Vector2(240, 400)

pausedQuitButtonOffset = Vector2(200, 550)
pausedQuitButtonTextPos = Vector2(325, 545)

# Game Over Buttons

gameOverPlatformOffsetTop = Vector2(120, 350)

gameOverReplayButtonOffset = Vector2(200, 400)
gameOverReplayButtonTextPos = Vector2(250, 395)

gameOverMenuButtonOffset = Vector2(200, 550)
gameOverMenuButtonTextPos = Vector2(240, 550)

gameOverQuitButtonOffset = Vector2(200, 700)
gameOverQuitButtonTextPos = Vector2(325, 695)

# Game Over Text
gameOverLeadingTextPos = Vector2(50, 50)
gameOverScoreTextPos = Vector2(350, 100)

# co-ordinates
x, y = 0, 1

# direction
DOWN = Vector2(0, 1)
RIGHT = Vector2(1, 0)
LEFT = Vector2(-1, 0)

# screen
tetrisDimensions = Vector2(10, 24)
blockSize = 40
gameScreenSize = Vector2(tetrisDimensions.x * blockSize, tetrisDimensions.y * blockSize)

# Side Bar
sideBarSize = Vector2(200, gameScreenSize.y)
# TODO: Maybe implemet top and bottom side bars too
whiteSquarePadding = Vector2(40, 75)

fullScreenSize = Vector2(gameScreenSize.x + sideBarSize.x * 2, gameScreenSize.y)
menuButtonSize = Vector2(fullScreenSize.x - menuPlayButtonOffset.x * 2, 100)
endGameButtonSize = Vector2(fullScreenSize.x - gameOverMenuButtonOffset.x * 2, 100)
gameOverPlatformSize = Vector2(fullScreenSize.x - gameOverPlatformOffsetTop.x * 2, 500)

# Drop Time Management
startingDelayTime = 1.5
decreasePerSec = 1 / 45
lowestDelayTime = 0.5

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

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        whiteSquarePadding.y + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                        3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
            pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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
           [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 2.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

            [pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         whiteSquarePadding.y + 1.5 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         3 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
                         1 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x)),
             pygame.Rect(whiteSquarePadding.x + sideBarSize.x + gameScreenSize.x + 2 / 5 * (sideBarSize.x - 2 * whiteSquarePadding.x),
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

# fonts
"""co_ordinates = self.find_block_coordinates(Vector2(x, y))
                    rect = pygame.Rect(co_ordinates.x, co_ordinates.y, self.blockSize, self.
                                       blockSize)
                    pygame.draw.rect(self.screen, constants.colorDict[self.matrix[y][x]], rect)"""
menu_font = pygame.font.SysFont("comic sans", 86)
paused_font = pygame.font.SysFont("comic sans", 64)

end_game_font_1 = pygame.font.SysFont("comic sans", 54)
end_game_font_2 = pygame.font.SysFont("comic sans", 154)

score_font = pygame.font.SysFont("arial", 40)
score_font_shift = Vector2(275, 10)
side_bar_font = pygame.font.SysFont("arial", 32)
stored_piece_font_shift = Vector2(135, 30)
next_piece_font_shift = Vector2(20, 30)
end_font1 = pygame.font.SysFont("arial", 128)
end_font2 = pygame.font.SysFont("arial", 64)
game_over_text = "GAME OVER"
