class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False

        if len(sides) == self.sides_count and self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f"Нельзя сменить цвет на ({r}, {g}, {b})")

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Неверное количество сторон или некорректные значения сторон.")

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14159)

    def get_square(self):
        return 3.14159 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1 and isinstance(sides[0], int):
            self.set_sides(*([sides[0]] * self.sides_count))
        else:
            self.set_sides(*([1] * self.sides_count))

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())      # [55, 66, 77]
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())