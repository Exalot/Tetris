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

# co-ordinates
x, y = 0, 1

# direction
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

# pieces
IPIECE = [[[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]],

          [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]]

JPIECE = [[[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
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

LPIECE = [[[0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
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

OPIECE = [[[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
          [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]]]

SPECIES = [[[0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
           [0, 0, 0, 5, 5, 0, 0, 0, 0, 0]],

          [[0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 5, 0, 0, 0, 0]]]

ZPIECE = [[[0, 0, 0, 6, 6, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 6, 6, 0, 0, 0, 0]],

          [[0, 0, 0, 0, 0, 6, 0, 0, 0, 0],
           [0, 0, 0, 0, 6, 6, 0, 0, 0, 0],
           [0, 0, 0, 0, 6, 0, 0, 0, 0, 0]]]

TPIECE = [[[0, 0, 0, 7, 7, 7, 0, 0, 0, 0],
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
    return [IPIECE, JPIECE, LPIECE, OPIECE, SPECIES, ZPIECE, TPIECE]

# indexes
IPIECEINDEX = 1
JPIECEINDEX = 2
LPIECEINDEX = 3
OPIECEINDEX = 4
SPECIESINDEX = 5
ZPIECEINDEX = 6
TPIECEINDEX = 7

# color dictionary
colorDict = {IPIECEINDEX: aqua,
             JPIECEINDEX: blue,
             LPIECEINDEX: orange,
             OPIECEINDEX: yellow,
             SPECIESINDEX: green,
             ZPIECEINDEX: red,
             TPIECEINDEX: purple}