
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f'Product ID: {self.product_id}')
        print(f'Procuct name: {self.name}')
        print(f'Price: {self.price}')
        

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        print(f'Product ID: #{self.product_id}, product name: {self.name}, price: {self.price}, size: {self.size}')
        
        
dress = Clothing("108704", "Maxi Dress", 69.99, "Small")
dress.display_info()
