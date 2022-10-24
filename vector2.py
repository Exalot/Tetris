import math

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return not self.x and self.y

    def __int__(self):
        return int(abs(self))

    def __float__(self):
        return float(abs(self))

    def __complex__(self):
        return complex(self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # vector stretching: (x1, y1) * a = (x1*a, y1*a)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(self.x * other, self.y * other)
        # vector multiplication: (x1, y1) * (x2, y2) = (x1*x2, y1*y2)
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        # vector compression: (x1, y1) / a = (x1/a, y1/a)
        if isinstance(other, int) or isinstance(other, float):
            return Vector2(int(self.x / int(other)), int(self.y / other))
        # vector compression: (x1, y1) / (x2, y2) = (x1/x2, y1/y2)
        elif isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)

    def __eq__(self, other):
        # magnitude comparison: sqrt(x1**2, y1**2) == a
        if isinstance(other, int):
            return self.magnitude == other
        # vector comparison: (x1, y1) / (x2, y2) = (x1/x2, y1/y2)
        elif isinstance(other, Vector2):
            return self.x == other.x and self.y == other.y

    def normalized(self):
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y
