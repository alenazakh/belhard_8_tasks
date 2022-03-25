class Tomato:
    index: int
    ripeness: str
    states = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index, ripeness=states[0]):
        self.index = index
        self.ripeness = ripeness

    def grow(self, states=states):
        for i in range(len(states)):
            if states[i] == self.ripeness:
                if self.ripeness != states[len(states) - 1]:
                    self.ripeness = states[i + 1]
                    break
                else:
                    break

    def is_ripe(self, states=states):
        if self.ripeness == states[len(states) - 1]:
            return True
        else:
            return False


if __name__ == '__main__':
    t1 = Tomato(1)
    print(type(t1.states))
    print(t1.states[len(t1.states) - 1])
    print(list(range(len(t1.states))))
    print(f"start {t1.ripeness}")
    t1.grow()
    print(f"next1 {t1.ripeness}")
    t1.grow()
    print(f"next2 {t1.ripeness}")
    if t1.is_ripe():
        print("уже созрел")
    else:
        print("еще не созрел")
    t1.grow()
    print(f"next3 {t1.ripeness}")
    if t1.is_ripe():
        print("уже созрел")
    else:
        print("еще не созрел")
    t1.grow()
    print(f"next4 {t1.ripeness}")
