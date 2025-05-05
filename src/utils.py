from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class InitPrintMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        cls_name = self.__class__.__name__
        args_repr = ", ".join(repr(arg) for arg in self.args) if hasattr(self, "args") else ""
        kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in self.kwargs.items()) if hasattr(self, "kwargs") else ""
        combined_repr = f"{cls_name}({args_repr}"
        if args_repr and kwargs_repr:
            combined_repr += f", {kwargs_repr}"
        elif kwargs_repr:
            combined_repr += kwargs_repr
        combined_repr += ")"
        return combined_repr


class Product(InitPrintMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs):
        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity
        self.args = (name, description, price, quantity)
        self.kwargs = kwargs
        super().__init__()

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
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество не должно быть отрицательным")
        self.__quantity = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Можно складывать только продукты одного класса")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: str,
        color: str,
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(
            name, description, price, quantity, efficiency=efficiency, model=model, memory=memory, color=color
        )

    def __str__(self):
        return (
            f"{self.name} ({self.model}), {self.efficiency}, {self.memory}, "
            f"{self.color}, {self.price} руб. Остаток: {self.quantity} шт."
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(
            name, description, price, quantity, country=country, germination_period=germination_period, color=color
        )

    def __str__(self):
        return (
            f"{self.name}, {self.country}, {self.germination_period} дней, "
            f"{self.color}, {self.price} руб. Остаток: {self.quantity} шт."
        )


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self._products)

    @property
    def products(self):
        return self._products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты или их наследников")
        self._products.append(product)
        Category.product_count += 1

    def get_products(self):
        return [str(product) for product in self._products]

    def get_products_list(self):
        return self._products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
