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

    def add_to_cart(self, inventory, inventory_item, amount_in_cart): # Funktion för att lägga till item till cart.
        if inventory_item not in inventory.inventory: # först kollar vi om itemet finns i inventory, gör den inte de returnar vi.
            return
        if inventory_item.amount_in_stock < amount_in_cart:
            return # om itemet finns måste amount_in_stock vara mer än 0 för att kunna läggas till.

        cartitem = CartItem(inventory_item.id, inventory_item.name, inventory_item.price, inventory_item.amount_in_cart) # går allt igenom ger vår cart item samma värden som inventory_item
        self.CartItems.append(cartitem)
        inventory_item.amount_in_stock -= amount_in_cart # vi säger även här att amount_in_stock minskar lika mycket med hur mycket som läggs till i amount_in_cart.
