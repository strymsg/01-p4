class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def show(self):
        print('Product:')
        print(f' Name: {self.name}')
        print(f' Description: {self.description}')
        print(f' Price: {self.price}')