import tomato


class TomatoBush:
    tomato_list: list
    copy_list = []

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in range(len(self.tomato_list)):
            self.tomato_list[i].grow()

    def all_are_ripe(self):
        if all(self.tomato_list[i].is_ripe() for i in range(len(self.tomato_list))):
            return True
        else:
            return False

    def give_away_all(self):
        copy_list = self.tomato_list.copy()
        self.tomato_list.clear()
        return copy_list


if __name__ == '__main__':
    t1 = tomato.Tomato(1)
    t2 = tomato.Tomato(2)
    t3 = tomato.Tomato(3)
    tb1 = TomatoBush(t1, t2, t3)
    print(tb1.tomato_list[0].index)
    print(tb1.tomato_list[1].index)
    print(tb1.tomato_list[2].index)
    tb1.grow_all()
    tb1.grow_all()
    print(tb1.all_are_ripe())
    tb1.grow_all()
    print(tb1.all_are_ripe())
    print(tb1.give_away_all())
    print(tb1.tomato_list)
