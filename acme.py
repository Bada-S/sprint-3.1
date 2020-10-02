import random

class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=.5):
        """"
        params
        `name` (string with no default)
        `price` (integer with default value 10)
        `weight` (integer with default value 20)
        `flammability` (float with default value 0.5)
        `identifier` (integer, automatically genererated as a random (uniform) number
        anywhere from 1000000 to 9999999, includisve)(inclusive).
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000,9999999)

    def stealability(self):
        """
        `stealability(self)` - calculates the price divided by the weight, and then
        returns a message: if the ratio is less than 0.5 return "Not so stealable...",
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
        and otherwise return "Very stealable!"
        """
        ratio = self.price/self.weight
        if(ratio<.5):
            return "Not so stealable..."
        if(.5<=ratio<1.0):
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        """
        `explode(self)` - calculates the flammability times the weight, and then
        returns a message: if the product is less than 10 return "...fizzle.", if it is
        greater or equal to 10 but less than 50 return "...boom!", and otherwise
        return "...BABOOM!!"
        """
        ratio = self.flammability * self.weight
        if(ratio<10):
            return "...fizzle."
        if(10<=ratio<50):
            return "...boom!"
        return "...BABOOM!!"
if __name__ == "__main__":
    product = Product("A cool toy")
    print(product.name, product.price, product.weight, product.flammability, product.identifier)
    print(product.stealability(), product.explode())

    product2 = Product("A very cool toy", price=100, weight=20, flammability=2.5)
    print(product2.name, product2.price, product2.weight, product2.flammability, product2.identifier)
    print(product2.stealability(), product2.explode())
