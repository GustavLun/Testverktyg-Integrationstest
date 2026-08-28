class Inventory: # Inventory klass som består av en lista
    def __init__(self):
        self.inventory = []

    def add_inventory(self,Inventory_item): #funktion till klassen som tillåter inventory_item att läggas till i listan.
        self.inventory.append(Inventory_item)


class Inventory_item: # En dummy klass som bara innehåller data till ett item.
    def __init__(self, id, name, price, amount_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock
