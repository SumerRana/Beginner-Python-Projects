import csv


class Item:
    rate = 0.8
    all = []

    def __init__(self, name, price,quantity=0):
        print(f"__int__ is working! for {name}")
        self.name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def post_discount(self):
        self.__price = self.__price * self.rate

    def app_increment(self, increment):
        self.__price = self.price + self.price * increment

    def total(self):
        return self.__price * self.quantity


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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value




    def __repr__(self): 
        return f"{self.__class__.__name__} ('{self.name}','{self.__price}','{self.quantity}'"
