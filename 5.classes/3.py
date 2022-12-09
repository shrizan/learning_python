class Point:
  # same as static value in java
  # it is called class level attribute
    default_color = "red"

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x,self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point(1, 2)
print(point.x, point.y)

point.z = 56
print(point.z)
zero = Point.zero()
print(zero.x)
