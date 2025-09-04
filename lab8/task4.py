class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their prices

    def add_item(self, name, price):
        """Adds an item to the cart."""
        self.items[name] = price

    def remove_item(self, name):
        """Removes an item from the cart if it exists."""
        if name in self.items:
            del self.items[name]

    def total_cost(self):
        """Returns the total cost of all items in the cart."""
        return sum(self.items.values())
