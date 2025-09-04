import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.5)

    def test_remove_item(self):
        self.cart.add_item("banana", 2.0)
        self.cart.remove_item("banana")
        self.assertNotIn("banana", self.cart.items)

    def test_remove_nonexistent_item(self):
        self.cart.add_item("orange", 1.0)
        self.cart.remove_item("pear")  # Should not raise an error
        self.assertIn("orange", self.cart.items)

    def test_total_cost_empty(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_total_cost_multiple_items(self):
        self.cart.add_item("milk", 2.5)
        self.cart.add_item("bread", 3.0)
        self.cart.add_item("eggs", 2.0)
        self.assertEqual(self.cart.total_cost(), 7.5)

    def test_add_item_overwrites(self):
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("apple", 2.0)  # Overwrite price
        self.assertEqual(self.cart.items["apple"], 2.0)
        self.assertEqual(self.cart.total_cost(), 2.0)

if __name__ == '__main__':
    unittest.main()