class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []


category = Category("Electronics", "Electronic devices")
product = Product("Smartphone", "A high-tech smartphone", 599.99, 10)

category.products.append(product)