class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Warehouse:
    def __init__(self, location):
        self.location = location
        self.inventory = {}

    def add_product(self, product):
        self.inventory[product.name] = product.quantity


class Shipping:
    def __init__(self, warehouse, destination):
        self.warehouse = warehouse
        self.destination = destination

    def ship_product(self, product_name):
        if product_name in self.warehouse.inventory:
            self.warehouse.inventory[product_name] -= 1
            print(f'Shipping {product_name} to {self.destination}')
        else:
            print(f'{product_name} is not in the warehouse inventory')


if __name__ == '__main__':
    warehouse = Warehouse('New York')
    warehouse.add_product(Product('iPhone', 10))
    shipping = Shipping(warehouse, 'Los Angeles')
    shipping.ship_product('iPhone')