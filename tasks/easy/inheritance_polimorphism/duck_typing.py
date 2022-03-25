"""
Создать 3 класса:

AmericanPerson, RussianPerson, GermanyPerson

в каждом классе определить метод i_love_science()

AmericanPerson.i_love_science() -> "I love science"
RussianPerson.i_love_science() - "Я люблю науку"
GermanyPerson.i_love_science() - "ich liebe Wissenschaft"


Написать функцию person_love_science, которая принимает объект и вызывает метод
i_love_science. Функция должна возвращать строку вида
"{obj.__class__.__name__} says that: {obj.i_love_science()}"

В блоке if __name__ == "__main__": сделать объекты трех классов и по очереди
передать их в функцию person_love_science.

https://www.youtube.com/watch?v=8o7ZKTvZpLc
"""


class AmericanPerson():
    def i_love_science(self):
        return'I love science'


class GermanyPerson:
    def i_love_science(self):
        return'Ich liebe Wissenschaft'


class RussianPerson:
    def i_love_science(self):
        return'Я люблю науку'


def person_love_science(obj):
    return(f"{obj.__class__.__name__} says that: {obj.i_love_science()}")


if __name__ == "__main__":
    Piter = AmericanPerson()
    Helmut = GermanyPerson()
    Anna = RussianPerson()
    person_love_science(Piter)
    person_love_science(Helmut)
    person_love_science(Anna)
