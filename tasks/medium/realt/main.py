import house
import person
import townhouse

if __name__ == '__main__':
    H1 = house.House('Serdich st., 8', 45.7, 55000.0)
    H2 = house.House('Lenina st., 17', 51.4, 30000.0)
    H1.increase_cost(1700.0)
    H2.decrease_cost(1000.0)
    T1 = townhouse.Townhouse('Grushevskaja, 2', 25000.0)
    T2 = townhouse.Townhouse('Jablonevaja, 14', 35000.0)
    T1.increase_cost(1500.0)
    T2.decrease_cost(1100.0)
    anna = person.Person('Anna', 37)
    anna.info()
    anna.earn_money(50000)
    anna.info()
    anna.make_deal(T1)
    anna.info()
    anna.make_deal(H1)
    anna.earn_money(70000)
    anna.info()
    anna.make_deal(H1)
    anna.info()
    anna.make_deal(H2)
    anna.info()
