class Point:
  # same as static value in java
  # it is called class level attribute
    default_color = "red"

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


point1 = Point(1, 2)
point2 = Point(3, 4)
print(point1+point2)
