import random


class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=.5):
        """"
        params
        `name` (string with no default)
        `price` (integer with default value 10)
        `weight` (integer with default value 20)
        `flammability` (float with default value 0.5)
        `identifier` randomly generated integer
        anywhere from 1000000 to 9999999, includisve)(inclusive).
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        `stealability(self)` - calculates how stealable a product is
        """
        ratio = self.price/self.weight
        if(ratio < .5):
            return "Not so stealable..."
        if(.5 <= ratio < 1.0):
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        """
        `explode(self)` - calculates how explosive a product is
        """
        ratio = self.flammability * self.weight
        if(ratio < 10):
            return "...fizzle."
        if(10 <= ratio < 50):
            return "...boom!"
        return "...BABOOM!!"


class BoxingGlove(Product):
    # subclass of Product
    def __init__(self, name):
        Product.__init__(self, name)
        self.weight = 10
        self.name = name

    def explode(self):
        # a boxing glove can not explode. Override this method
        return "...it's a glove"

    def punch(self):
        """
        return how much a punch hurts
        """
        if(self.weight < 5):
            return "That tickles."
        elif(5 <= self.weight < 15):
            return "Hey that hurt!"
        return "Ouch!"

if __name__ == "__main__":
    product = Product("A cool toy")
    print(product.name, product.price, product.weight, product.flammability,
          product.identifier)
    print(product.stealability(), product.explode())

    product2 = Product("Awesome toy", price=100, weight=20, flammability=2.5)
    print(product2.name, product2.price, product2.weight,
          product2.flammability, product2.identifier)
    print(product2.stealability(), product2.explode())
