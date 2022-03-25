"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:
    __x: int
    __y: int
    a = 555

    def __init__(self, __x, __y):
        self.__x = __x
        self.__y = __y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def move(self, delta_x, delta_y):
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y


game_obj1 = GameObject(53, 17)
print(game_obj1.x)
print(game_obj1.y)
game_obj1.move(4, -10)
print(game_obj1.x)
print(game_obj1.y)
