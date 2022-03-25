import gardener
import tomato
import tomato_bush

if __name__ == '__main__':
    t1 = tomato.Tomato(1)
    t2 = tomato.Tomato(2)
    t3 = tomato.Tomato(3)
    t4 = tomato.Tomato(4)
    t5 = tomato.Tomato(5)
    tb1 = tomato_bush.TomatoBush(t1, t2, t3)
    tb2 = tomato_bush.TomatoBush(t4, t5)
    gard1 = gardener.Gardener('Peter', tb1, tb2)
    gard1.work()
    gard1.work()
    print(gard1.harvest())
    gard1.work()
    print(gard1.harvest())
    print(tb1.tomato_list)
    print(tb2.tomato_list)
