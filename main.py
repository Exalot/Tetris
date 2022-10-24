"""
Main file of project
"""

import pygame
import random
import constants
import copy

from vector2 import Vector2


class TetrisAlgorithm(object):
    """
    Runs the Tetris game and demonstrates the algorithm
    """

    def __init__(self) -> None:
        self.tetrisDimensions = Vector2(10, 24)
        self.blockSize = 40
        self.blockOffset = Vector2(0, 0)
        self.screenSize = Vector2(self.tetrisDimensions.x * self.blockSize, self.tetrisDimensions.y * self.blockSize)
        self.screen = pygame.display.set_mode(self.screenSize.to_tuple())
        self.clock = pygame.time.Clock()
        self.matrix = [[0 for i in range(self.tetrisDimensions.x)] for j in range(self.tetrisDimensions.y)]
        self.pieceList = constants.get_pieces()
        self.rotation = 0
        self.movingPieceTemplate = []
        self.movingPieceCoordinates = []
        self.game_over = False
        self.score = 0

    def __print_matrix(self) -> None:
        for row in self.matrix:
            print(row)

    def __get_moving_piece_coordinate(self) -> list[Vector2]:
        return copy.deepcopy(self.movingPieceCoordinates)

    def __get_moving_piece_future_coordinate(self, direction: Vector2) -> list[Vector2]:
        return [piece_coordinate + direction for piece_coordinate in self.movingPieceCoordinates]

    def end_game(self) -> None:
        """
        ends game
        """
        pass
        """
        self.draw_matrix()
        # self.screen.blit(scoreText, (self.screenSize[constants.x] - 150, 5))
        endText1 = constants.end_font1.render(constants.game_over_text, True, constants.white)
        endText2 = constants.end_font2.render(f"You achieved a score of: {self.score}", True, constants.white)
        """

    def process_piece_spawn(self, piece_list: list[list[list[int]]]) -> None:
        """
        finds the co-ordinates of the new moving pieces and add their colors to the matrix
        :param piece_list: The piece selected from the list of pieces
        """
        for y in range(len(piece_list[0][self.rotation])):
            for x in range(len(piece_list[0][self.rotation][y])):
                if piece_list[0][self.rotation][y][x]:
                    if not self.matrix[y][x]:
                        self.movingPieceCoordinates.append(Vector2(x, y))
                        self.matrix[y][x] = piece_list[0][self.rotation][y][x]
                    else:
                        self.game_over = True

    def spawn_piece(self) -> None:
        """
        spawns a piece at the top of the matrix
        """
        self.movingPieceCoordinates.clear()
        self.rotation = 0
        self.blockOffset = Vector2(0, 0)
        if len(self.pieceList) == 0:
            self.pieceList = constants.get_pieces()
        self.movingPieceTemplate = random.choice(self.pieceList)
        self.pieceList.remove(self.movingPieceTemplate)
        self.process_piece_spawn(self.movingPieceTemplate)

    def can_move_direction(self, direction: Vector2) -> bool:
        """
        Checks if the moving piece can move down any further
        :param direction: the direction of the movement
        :return: boolean representing if the selected piece can move down
        """
        for futurePiece in self.__get_moving_piece_future_coordinate(direction):
            if futurePiece.x < 0:
                return False
            if (futurePiece.x, futurePiece.y >= 0) and not (futurePiece.x < self.tetrisDimensions.x and futurePiece.y <
                                                            self.tetrisDimensions.y):
                return False
            elif self.matrix[futurePiece.y][futurePiece.x] and True not in [Vector2(futurePiece.x, futurePiece.y) ==
                                                                            movingBlock for movingBlock in
                                                                            self.movingPieceCoordinates]:
                return False
        return True

    def move_direction(self, direction: Vector2) -> None:
        """
        moves the moving piece in specified direction
        :param direction: the direction of the movement
        """
        color = self.matrix[self.movingPieceCoordinates[0].y][self.movingPieceCoordinates[0].x]
        new_coordinates = self.__get_moving_piece_future_coordinate(direction)
        for movingPiece in self.movingPieceCoordinates:
            self.matrix[movingPiece.y][movingPiece.x] = 0
        for newPiece in new_coordinates:
            self.matrix[newPiece.y][newPiece.x] = color
        self.movingPieceCoordinates = new_coordinates
        self.blockOffset += direction

    def hard_drop(self) -> None:
        """
        Hard drops the current piece
        """
        while self.can_move_direction(constants.DOWN):
            self.move_direction(constants.DOWN)
        self.spawn_piece()

    def __cleanMovingPieces(self) -> None:
        for movingCoordinate in self.movingPieceCoordinates:
            self.matrix[movingCoordinate.y][movingCoordinate.x] = 0

    # TODO: FIX THIS
    def rotate(self, clockwise: bool) -> None:
        """
        rotates the selected piece
        """
        rotationMove = self.movingPieceTemplate[1][self.rotation]
        coordinateTemp = copy.deepcopy(self.movingPieceCoordinates)
        # not square do this else dont
        for i in range(len(coordinateTemp)):
            coordinateTemp[i] += rotationMove[i]
        if self.rotationValid(coordinateTemp):
            color = self.matrix[self.movingPieceCoordinates[0].y][self.movingPieceCoordinates[0].x]
            self.__cleanMovingPieces()
            self.movingPieceCoordinates = coordinateTemp
            for coordinate in self.movingPieceCoordinates:
                self.matrix[coordinate.y][coordinate.x] = color
            if clockwise:
                self.rotation = (self.rotation + 1) % len(self.movingPieceTemplate[1])
            else:
                if self.rotation != 0:
                    self.rotation = (self.rotation - 1) % len(self.movingPieceTemplate[0])
                else:
                    self.rotation = len(self.movingPieceTemplate[0]) - 1

    def rotationValid(self, newMovingCoordinates: list[Vector2]) -> bool:
        matrixTemp = copy.deepcopy(self.matrix)
        for movingCordinate in self.movingPieceCoordinates:
            matrixTemp[movingCordinate.y][movingCordinate.x] = 0
        for coordinate in newMovingCoordinates:
            if coordinate.x < 0:
                return False
            elif (coordinate.x, coordinate.y >= 0) and not (coordinate.x < self.tetrisDimensions.x and coordinate.y <
                                                            self.tetrisDimensions.y):
                return False
            elif matrixTemp[coordinate.y][coordinate.x]:
                return False

        return True

    def find_block_coordinates(self, position: Vector2) -> Vector2:
        """
        helper function to find the x and y co-ordinates of block in matrix
        :param position: A vector2 representing the x, y location of the block
        :return: tuple representing x, y co-ordinates of block
        """
        return position * self.blockSize

    def draw_matrix(self) -> None:
        """
        Draws the matrix on the screen
        """
        self.screen.fill(constants.black)
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] != 0:
                    co_ordinates = self.find_block_coordinates(Vector2(x, y))
                    rect = pygame.Rect(co_ordinates.x, co_ordinates.y, self.blockSize, self.
                                       blockSize)
                    pygame.draw.rect(self.screen, constants.colorDict[self.matrix[y][x]], rect)

    def process_filled_lines(self) -> None:
        filledLineIndexes = self.check_filled_line()
        if len(filledLineIndexes) > 0:
            color = self.matrix[self.movingPieceCoordinates[0].y][self.movingPieceCoordinates[0].x]
            for coordinate in self.movingPieceCoordinates:
                self.matrix[coordinate.y][coordinate.x] = 0
            self.score += len(filledLineIndexes)
            filledLineIndexes.sort()
            for index in filledLineIndexes:
                self.matrix.pop(index)
                self.matrix.insert(0, [0 for i in range(self.tetrisDimensions.y)])
            for coordinate in self.movingPieceCoordinates:
                self.matrix[coordinate.y][coordinate.x] = color

    def check_filled_line(self) -> list[int]:
        lineIndexes = []
        for y in range(len(self.matrix)):
            if self.check_horizontal_line_helper(y):
                lineIndexes.append(y)
        return lineIndexes

    def check_horizontal_line_helper(self, lineIndex) -> bool:
        line = self.matrix[lineIndex]
        for num in line:
            if num == 0:
                return False
        return True

    def main(self) -> None:
        """
        Runs the game
        """
        pygame.init()
        pygame.display.set_caption("Tetris Algorithm")
        self.spawn_piece()
        running = True
        # game loop
        while running:
            print(self.score)
            if not self.game_over:
                # event loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        running = False
                    elif event.type == pygame.KEYDOWN and constants.debugMode:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            running = False
                        elif event.key == pygame.K_SPACE:
                            self.hard_drop()
                            # TODO: Make hard drop set rotation to 0
                        elif event.key == pygame.K_DOWN:
                            if self.can_move_direction(constants.DOWN):
                                self.move_direction(constants.DOWN)
                        elif event.key == pygame.K_RIGHT:
                            if self.can_move_direction(constants.RIGHT):
                                self.move_direction(constants.RIGHT)
                        elif event.key == pygame.K_LEFT:
                            if self.can_move_direction(constants.LEFT):
                                self.move_direction(constants.LEFT)
                        elif event.key == pygame.K_x:
                            self.rotate(True)
                            pass  # TODO: Implement clockwise rotation
                        elif event.key == pygame.K_z:
                            self.rotate(False)
                            pass  # TODO: Implement counter clockwise rotation
                self.process_filled_lines()
                self.draw_matrix()
                score_text = constants.score_font.render(f"Score: {self.score}", True, constants.white)
                self.screen.blit(score_text, (self.screenSize.x - constants.score_font_shift.x,
                                              constants.score_font_shift.y))
            else:
                print("Game Over")
                for event in pygame.event.get():
                    if event.key == pygame.QUIT:
                        pygame.quit()
                        running = False
                    elif event.key == pygame.K_ESCAPE and constants.debugMode:
                        pygame.quit()
                        running = False
            pygame.display.update()
            self.clock.tick(120)


if __name__ == '__main__':
    game = TetrisAlgorithm()
    game.main()
