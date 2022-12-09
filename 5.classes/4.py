class Point:
  # same as static value in java
  # it is called class level attribute
    default_color = "red"

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x,self.y})")

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point.zero()
print(point)
