from asyncore import read
import csv
from sys import float_repr_style

class Item:
    rate = 0.8
    all = []

    def __init__(self, name, price,quantity):
        print(f"__int__ is working! for {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def total(self):
        return self.price * self.quantity

    def post_discount(self):
        self.price = self.price * self.rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            item = list(reader)

        for i in item:
            Item(name=i.get('name'),price=int(i.get('price')),quantity=i.get('quantity'))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else: 
            return False



    def __repr__(self): 
        return f"{self.__class__.__name__} ('{self.name}','{self.price}','{self.quantity}'"

class phone(Item):
     def __init__(self, name: str, price: float, quantity: int, broken=0):
        all = []
        super().__init__(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken = broken

        phone.all.append(self)

phone1 = phone("ph1", 300, 6, 1)
print(phone1.total())
phone2 = phone("ph2", 550, 4, 1)
print(phone2.total())

print(phone.all)






















# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)


# Item.instantiate_from_csv()
# print(Item.all)
























































# item1 = Item("phone", 100, 5)
# # item1.name = "phone"
# # item1.price = 100
# # item1.quantity = 5
# item1.cost = item1.total()

# print(item1.name)


# item2 = Item("Laptop", 1000, 4)
# # item2.name = "Laptop"
# # item2.price = 1000
# # item2.quantity = 4
# item2.cost = item2.total()

# print(item1.cost + item2.cost)
# item1.post_discount()
# print(item1.cost + item2.cost)
# print(item1.price)

# item2.rate = 0.4
# item2.post_discount()
# print(item2.price)