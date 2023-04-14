import imp
from Item import Item

class phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken=0):
        all = []
        super().__init__(name, price, quantity)

        self._name = name
        self.price = price
        self.quantity = quantity
        self.broken = broken

        phone.all.append(self)

    @property
    def name(self):
        return self._name
        
