from src.kundvagn.inventory import Inventory_item


class CartItem: # En klass som nästan är en kopia av item klassen men har member variable amount_in_cart
    def __init__(self, id, name, price, amount_in_cart):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_cart = amount_in_cart

class ShoppingCart: # Enkel klass för shoppingcart som är en tom lista.
    def __init__(self):
        self.CartItems = []

    def add_to_cart(self, Inventory, inventory_item, amount_in_cart): # Funktion för att lägga till item till cart.
        if inventory_item not in Inventory.inventory: # först kollar vi om itemet finns i inventory, gör den inte de returnar vi.
            return
        for x in range(amount_in_cart): # baserat på hur många item "x" vi läggs så många till i amount in cart.
            self.CartItems.append(Inventory_item)
            inventory_item.amount_in_stock -= amount_in_cart # vi säger även här att amount_in_stock minskar lika mycket med hur mycket som läggs till i amount_in_cart.
