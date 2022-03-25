import house


class Townhouse(house.House):

    def __init__(self, address, cost, area=60):
        super().__init__(address, area, cost)
