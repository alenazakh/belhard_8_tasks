"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year
print(type(CURRENT_YEAR))


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, __author, __title, __year):
        if isinstance(__author, str):
            self.__author = __author
        else:
            raise ValueError("Не верное значение.")
        if isinstance(__title, str):
            self.__title = __title
        else:
            raise ValueError("Не верное значение.")
        if isinstance(__year, int):
                if 0 < __year <= CURRENT_YEAR:
                    self.__year = __year
                elif __year <= 0:
                    raise ValueError("Мы не храним книг, изданных до нашей эры.")
                else:
                    raise ValueError("Мы не храним книги из будущего.")
        else:
            raise ValueError("Не верное значение.")

    def sorting_book(self):
        pass

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, str):
            self.__author = new_author
        else:
            raise ValueError("Не верное значение.")

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self.__title = new_title
        else:
            raise ValueError("Не верное значение.")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, int):
            if 0 < new_year <= CURRENT_YEAR:
                self.__year = new_year
            elif new_year <= 0:
                raise ValueError("Мы не храним книг, изданных до нашей эры.")
            else:
                raise ValueError("Мы не храним книги из будущего.")
        else:
            raise ValueError("Не верное значение.")


Book1 = BookCard('Габирэль Гарсия Маркес', 'Сто лет одиночества', 1967)
Book2 = BookCard('Пауло Коэльо', 'Алхимик', 1988)
Book3 = BookCard('Маргарет Митчелл', 'Унесенные ветром', 1936)
# Book41 = BookCard(1001, 'Унесенные ветром', 1936)
# Book42 = BookCard('Маргарет Митчелл', 1002, 1936)
# Book43 = BookCard('Маргарет Митчелл', 'Унесенные ветром', -1936)
# Book44 = BookCard('Маргарет Митчелл', 'Унесенные ветром', 2936)
# Book45 = BookCard('Маргарет Митчелл', 'Унесенные ветром', '1936')
# print(Book1.__author) - ошибка
print(Book1.author)
print(Book2.title)
print(Book3.year)
Book1.author = 'Габирэль Гарсия Маркес NEW'
Book1.title = 'Сто лет одиночества NEW'
Book1.year = 1968
print(str(Book1.author) + ' ' + str(Book1.title) + ' ' + str(Book1.year))
# Book2.title = 1002
# Book2.year = -1936
# Book3.year = 2025
