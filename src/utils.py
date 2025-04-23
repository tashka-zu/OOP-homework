class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не должна быть отрицательной")
        else:
            self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError()
        else:
            self.__quantity = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError()

        total_price = self.price * self.quantity + other.price * other.quantity
        total_quantity = self.quantity + other.quantity

        return Product(
            name="Суммарный продукт",
            description="Суммарный продукт для расчета общей стоимости",
            price=total_price / total_quantity,
            quantity=total_quantity,
        )


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError()
        self.__products.append(product)
        Category.product_count += 1

    def get_products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


# Пример использования
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Складываем продукты
    total_product = product1 + product2 + product3
    total_cost = total_product.price * total_product.quantity
    print(f"Общая стоимость всех товаров на складе: {total_cost} руб.")

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    for product_info in category1.get_products():
        print(product_info)

    print(category1)
