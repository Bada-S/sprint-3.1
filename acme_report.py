from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    i = 1
    while i in range(num_products):
        ad_num = randint(0, 4)
        no_num = randint(0, 4)
        name = ADJECTIVES[ad_num] + ' ' + NOUNS[no_num]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(.5, 2.5)
        new_product = Product(name, price, weight, flammability)
        products.append(new_product)
        i = i+1
    return products


def inventory_report(products):
    # TODO - your code! Loop over the products to calculate the report.
    unique_names = 0
    total_price = 0
    total_weight = 0
    total_flammability = 0
    i = 0
    X = 0
    for a in range(5):
        for b in range(5):
            for i in range(30):
                if(products[i-1].name == ADJECTIVES[a] + ' ' + NOUNS[b]):
                    X = 1
            if(X == 1):
                unique_names = unique_names+1
                X = 0

    for i in range(30):
        total_price = total_price + products[i-1].price
    for i in range(30):
        total_weight = total_weight + products[i-1].weight
    for i in range(30):
        total_flammability = total_flammability + products[i-1].flammability
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ' + str(unique_names))
    print('Average price: ' + str(total_price/30))
    print('Average weight: ' + str(total_weight/30))
    print('Average flammability: ' + str(total_flammability/30))

if __name__ == '__main__':
    inventory_report(generate_products())
