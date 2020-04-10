# acme_test.py
# Part 5

import unittest
# https://docs.python.org/3/library/unittest.html
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
# test default values
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product A')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight is 20."""
        prod = Product('Test Product B')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability is 0.5."""
        prod = Product('Test Product C')
        self.assertEqual(prod.flammability, 0.5)

# test class methods stealability and explode
    def test_product_method_steal(self):
        """Test class method stealability"""
        prod = Product('Test Stolen Product')
        self.assertIsNotNone(prod.stealability)

    def test_product_method_explode(self):
        """Test class method explode"""
        prod = Product('Test Exploded Product')
        self.assertIsNotNone(prod.explode)

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
# test at least 2 methods
    def test_default_num_products(self):
        """Test that the default number of products generated is 30"""
        product_list = generate_products()
        self.assertEqual(len(product_list), 30)

    def test_legal_names(self):
        """Test that the generated names are official Acme names"""
        product_list = generate_products()
        for item in product_list:
            name_half = item.name.split(" ")
            self.assertIn(name_half[0], ADJECTIVES)
            self.assertIn(name_half[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
