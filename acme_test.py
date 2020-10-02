import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_product_weight(self):
        #test default product weight = 20
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    def test_default_product_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, .5)



if __name__ == '__main__':
    test_product = Product('test', price=15, weight=25, flammability=2)
    print(test_product.explode(), test_product.stealability())
    unittest.main()
