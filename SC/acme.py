#acme.py
from random import randint


# Part 1
class Product():
    """
    Class for products of Acme Co.
    """
    def __init__(self, name, price= 10, weight= 20, flammability= 0.5):
        """
        Variables: name, price (has default), weight (has default),
        flammability (has default), identifier (auto generated random number)
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)

# Part 2
    def stealability(self):
        """
        Product class method to calculate how tempting product is to steal
        Calculates the price divided by the weight
        Returns string message
        """
        stealability = (self.price / self.weight)
        if (stealability < 0.5):
            return "Not so stealable..."
        elif ((stealability >= 0.5) & (stealability < 1.0))
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """
        Product class method to calculate explosion size of product
        Calculates the flammability times the weight
        Returns string message
        """
        explode = (self.flammability * self.weight)
        if (explode < 10):
            return "...fizzle."
        elif ((explode >= 10) & (explode < 50))
            return "...boom!"
        else:
            return: "...BABOOM!!"


# Part 3
class BoxingGlove(Product):
    """
    Subclass of product
    Same Variables (weight has new default)
    """
    def __init__(self, name, price= 10, weight= 10, flammability= 0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)

    def explode(self):
    """
    Overwrites product class method to return a constant string message
    """
        return "...it's a glove"

    def punch(self):
    """
    Subclass method
    Calculates glove pain factor
    Returns string message
    """
        if (self.weight < 5):
            return "That tickles."
        elif ((self.weight >= 5) & (self.weight < 15)):
            return "Hey that hurt!"
        else:
            return "OUCH!"
        
