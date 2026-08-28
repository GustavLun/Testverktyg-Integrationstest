from src.kundvagn.inventory import *
from src.kundvagn.shopping_cart import *
import pytest

@pytest.mark.integration
def test_add_out_of_stock_item():
    shopping_cart = ShoppingCart()
    inventory = Inventory()

    item = Inventory_item(1, "gurka", 50, 2) # vi deklarerar en vara gurka som de finns 2 av
    inventory.add_inventory(item) # Vi lägger till den i vår inventory.


    shopping_cart.add_to_cart(inventory, item, 3) #vi försöker ta fler gurkor än vad de finns i inventory vilket inte ska gå.

    assert item not in shopping_cart.CartItems