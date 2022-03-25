class House:
    address: str
    area: float
    cost: float

    def __init__(self, address, area, cost):
        self.address = address
        self.area = float(area)
        self.cost = float(cost)

    def increase_cost(self, change_cost):
        change_cost = float(change_cost)
        self.cost += change_cost

    def decrease_cost(self, change_cost):
        change_cost = float(change_cost)
        self.cost -= change_cost
