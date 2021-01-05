import pygame
import random
import constants
import copy


class TetrisAlgorithm(object):
    """
    Runs the Tetris game and demonstrates the algorithm
    """

    def __init__(self):
        self.tetrisDimensions = (10, 24)
        self.blockSize = 40
        self.screenSize = (screenSizeX, screenSizeY) = (
            self.tetrisDimensions[constants.x] * self.blockSize, self.tetrisDimensions[constants.y] * self.blockSize)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock = pygame.time.Clock()
        self.matrix = [[0 for i in range(self.tetrisDimensions[constants.x])] for j in range(self.tetrisDimensions[
                                                                                                 constants.y])]
        self.pieceList = constants.get_pieces()
        self.rotation = 0
        self.movingPieceTemplate = []
        self.movingPieceCoordinates = []
        self.rigidPieceCoordinates = []

    def __print_matrix(self):
        for row in self.matrix:
            print(row)

    def __get_moving_piece_coordinate(self):
        return self.movingPieceCoordinates

    def process_piece_spawn(self, piece_list: list[list[list[int]]]):
        """
        finds the co-ordinates of the new moving pieces and add their colors to the matrix
        :param piece_list: The piece selected from the list of pieces
        """
        for y in range(len(piece_list[self.rotation])):
            for x in range(len(piece_list[self.rotation][y])):
                if piece_list[self.rotation][y][x]:
                    self.movingPieceCoordinates.append((x, y))
                    self.matrix[y][x] = piece_list[self.rotation][y][x]

    def spawn_piece(self):
        """
        spawns a piece at the top of the matrix
        """
        self.movingPieceCoordinates.clear()
        self.rotation = 0
        if len(self.pieceList) == 0:
            self.pieceList = constants.get_pieces()
        self.movingPieceTemplate = random.choice(self.pieceList)
        self.pieceList.remove(self.movingPieceTemplate)
        self.process_piece_spawn(self.movingPieceTemplate)

    def can_move_direction(self, direction: tuple[int, int]) -> bool:
        """
        Checks if the moving piece can move down any further
        :param direction: the direction of the movement
        :return: boolean representing if the selected piece can move down
        """
        newCoordinates = self.__get_moving_piece_coordinate()
        for x, y in newCoordinates:
            if not (x < self.tetrisDimensions[constants.x] - 1 and y < self.tetrisDimensions[constants.y] - 1):
                return False
        return True

    def move_direction(self, direction: tuple[int, int]):
        """
        moves the moving piece in specified direction
        :param direction: the direction of the movement
        """
        color = self.matrix[self.movingPieceCoordinates[0][constants.y]][self.movingPieceCoordinates[0][constants.x]]
        oldCoordinates = copy.deepcopy(self.__get_moving_piece_coordinate())
        newCoordinates = copy.deepcopy(self.__get_moving_piece_coordinate())
        for x, y in self.movingPieceCoordinates:
            self.matrix[y][x] = 0
        for coordinateIndex in range(len(newCoordinates)):
            newCoordinates[coordinateIndex] = (oldCoordinates[coordinateIndex][constants.x] + direction[constants.x],
                                               oldCoordinates[coordinateIndex][constants.y] + direction[constants.y])
        for x, y in newCoordinates:
            self.matrix[y][x] = color
        self.movingPieceCoordinates = newCoordinates

    def hard_drop(self):
        """
        Hard drops the current piece
        """
        while self.can_move_direction(constants.DOWN):
            self.move_direction(constants.DOWN)
        self.spawn_piece()

    def rotate(self):
        """
        rotates the selected piece
        """
        self.rotation = (self.rotation + 1) % len(self.movingPieceTemplate)

    def find_block_coordinates(self, x: int, y: int) -> tuple[int, int]:
        """
        helper function to find the x and y co-ordinates of block in matrix
        :param x: x index of block
        :param y: y index of block
        :return: tuple representing x, y co-ordinates of block
        """
        return self.blockSize * x, self.blockSize * y

    def draw_matrix(self):
        """
        Draws the matrix on the screen
        """
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] != 0:
                    co_ordinates = self.find_block_coordinates(x, y)
                    rect = pygame.Rect(co_ordinates[constants.x], co_ordinates[constants.y], self.blockSize, self.
                                       blockSize)
                    pygame.draw.rect(self.screen, constants.colorDict[self.matrix[y][x]], rect)

    def main(self):
        """
        Runs the game
        """
        pygame.init()
        pygame.display.set_caption("Tetris Algorithm")
        running = True
        # game loop
        while running:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.KEYDOWN and constants.debugMode:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        running = False
                    elif event.key == pygame.K_TAB:
                        self.spawn_piece()
                    elif event.key == pygame.K_SPACE:
                        self.hard_drop()
            self.draw_matrix()
            pygame.display.update()
            self.clock.tick(120)


if __name__ == '__main__':
    game = TetrisAlgorithm()
    game.main()
