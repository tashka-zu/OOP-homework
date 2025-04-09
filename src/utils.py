class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product: Product):
        self.products.append(product)
        Category.product_count += 1


# Пример использования
category = Category("Электроника", "Электрические приборы")
product = Product("Техника", "Ноутбук", 30000.39, 10)

category.add_product(product)
