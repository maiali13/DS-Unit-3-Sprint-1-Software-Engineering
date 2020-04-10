# acme_report.py
# Part 4
"""
Modules to generate random products and report their properties
"""
import random
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_products=30):
    """
    Generates number of random products (default num_products = 30)
    Returns them as a list
    """
    product_list = []
    for i in range(num_products):
        noun =
        name = choice(ADJECTIVES) + " " + choice(NOUNS)
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        stat = Product(name, price, weight, flammability)
        product_list.append(stat)
    return product_list

def inventory_report(product_list):
    """
    Returns information on the generated products
    Prints the number of unique product names in the product list
    Average price, weight, and flammability of listed products
    """
# number of unique products
    names_list = []
    price_list = []
    weight_list = []
    flammability_list = []
    for item in product_list:
        names_list.append(item.name)
        price_list.append(item.price)
        weight_list.append(item.weight)
        flammability_list.append(item.flammability)
# mean product stats
    price_avg = sum(price_list) / len(price_list)
    weight_avg = sum(weight_list) / len(weight_list)
    flammability_avg = sum(flammability_list) / len(flammability_list)
    print("Acme Co. Official Inventory Report")
    print(f"Number of unique products:", len(set(names_list)))
    print(f"The average product price is:", price_avg)
    print(f"The average product weight is:", weight_avg)
    print(f"The average product flammability is:", flammability_avg)
    return


if __name__ == '__main__':
    inventory_report(generate_products())
