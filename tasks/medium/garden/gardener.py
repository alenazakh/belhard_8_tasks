import tomato
import tomato_bush


class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)     # или arg[0] если передается общим списком после name    (name, (.....,,,,))

    def work(self):
        for i in range(len(self.plants)):
            self.plants[i].grow_all()

    def harvest(self):
        copy_list = []
        if all(self.plants[i].all_are_ripe() for i in range(len(self.plants))):
            for item in self.plants:
                copy_list.append(item.give_away_all())
            return sum(copy_list, [])                      # из списка списков делает список
        else:
            print("Не все томаты созрели.")
            return None


if __name__ == '__main__':
    t1 = tomato.Tomato(1)
    t2 = tomato.Tomato(2)
    t3 = tomato.Tomato(3)
    t4 = tomato.Tomato(4)
    t5 = tomato.Tomato(5)
    tb1 = tomato_bush.TomatoBush(t1, t2, t3)
    tb2 = tomato_bush.TomatoBush(t4, t5)
    gard1 = Gardener('Peter', tb1, tb2)
    gard1.work()
    gard1.work()
    print(gard1.harvest())
    gard1.work()
    print(gard1.harvest())
    print(tb1.tomato_list)
    print(tb2.tomato_list)
