class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age, money=0, realty=None):
        if realty is None:
            realty = []
        self.name = name
        self.age = age
        self.money = float(money)
        self.realty = realty

    def info(self):
        print(f"Имя: {self.name}.")
        print(f"Возраст: {self.age}.")
        print_list = []
        for i in range(len(self.realty)):
            print_list.append(f"{self.realty[i].__class__.__name__} ({self.realty[i].address}, {self.realty[i].area})")
        if not print_list:
            print("Недвижимость в собственности: нет.")
        else:
            print("Недвижимость в собственности:")
            print(*print_list, sep='\n')
        print(f"Деньги на счетах: {self.money}.")

    def earn_money(self, extra_money):
        extra_money = float(extra_money)
        self.money += extra_money

    def make_deal(self, arg):
        if self.money >= arg.cost:
            self.money -= arg.cost
            self.realty.append(arg)
        else:
            print("У Вас недостаточно денег для покупки. Будем рады Вас видеть вновь.")
