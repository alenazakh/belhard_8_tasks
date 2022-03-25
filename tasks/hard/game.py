"""
Описать класс Warrior:

- атрибут name - имя юнита (тип str)
- атрибут health_points - показатель здоровья (тип int от 0 до 100)
- магический метод __init__, который принимает аргумент name и создает юнита со
  100 health_points
- метод hit, который принимает аргумент other типа Warrior. Если значение
 health_points у other <= 0 бросить исключение ValueError("Второй воин мертв").
 Если нет, то снять у other 20 health_points и вывести на экран сообщение
 "{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP"

Описать класс Arena:

- атрибут warriors - все воины на арене (тип list)
- магический метод __init__, который принимает необязательный аргумент warriors.
 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
 пустым списком.
- метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
 "{warrior.name} участвует в битве"
- метод choose_warrior, который не принимает аргументов и возвращает случайного
  воина из warriors
- метод battle, который не принимает аргументов и симулирует битву. Сперва
 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
 исключение ValueError("Количество воинов на арене должно быть больше 1").
 Битва продолжается, пока на арене не останется только один воин. Сперва
 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
 из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
 Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
 Вернуть данного воина из метода battle.
"""

import random


class Warrior:
    name: str
    health_points: int   # (0,100)

    def __init__(self, name):
        self.name = name
        self.health_points = 100

    def hit(self, other):
        if other.health_points > 0:
            other.health_points = other.health_points - 20
            print(f"{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP.")
        else:
            raise ValueError("Второй воин мертв.")


class Arena:
    warriors = list()

    def __init__(self, warriors=None):
        if warriors is None:
            warriors = []
        self.warriors = warriors

    def print_w(self):
        print(self.warriors)

    def add_warrior(self, new_warrior):
        if new_warrior in self.warriors:
            raise ValueError("Воин уже на арене.")
        else:
            self.warriors.append(new_warrior)
            print(f"{new_warrior.name} участвует в битве.")

    def choose_warrior(self):
        return self.warriors[random.randrange(0, len(self.warriors))]

    def battle(self):
        if len(self.warriors) > 1:
            while len(self.warriors) > 1:
                attack = self.choose_warrior()
                defender = self.choose_warrior()
                if defender == attack:
                    while defender == attack:
                        defender = self.choose_warrior()
                attack.hit(defender)
                if defender.health_points <= 0:
                    self.warriors.remove(defender)
                    print(f"{defender.name} пал в битве.")
            print(f"Победил воин: {self.warriors[0].name}.")
            return self.warriors[0]
        else:
            raise ValueError("Количество воинов на арене должно быть больше 1.")


if __name__ == "__main__":
    sparta = Arena()
    spartak = Warrior('Спартак')
    krics = Warrior('Крикс')
    cast = Warrior('Каст')
    enomay = Warrior('Эномай')
    publipor = Warrior('Публипор')
    commod = Warrior('Коммод')
    sparta.add_warrior(spartak)
    sparta.add_warrior(krics)
    sparta.add_warrior(cast)
    sparta.add_warrior(enomay)
    sparta.add_warrior(publipor)
    sparta.add_warrior(commod)
    sparta.battle()
