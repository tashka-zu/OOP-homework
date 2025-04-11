from src.utils import Category, Product


def test_create_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    assert category.name == "Электроника"
    assert category.description == "Электрические приборы"
    assert category.get_products() == []
    assert Category.category_count == 1

    category.description = "Обновленные электрические приборы"
    assert category.description == "Обновленные электрические приборы"


def test_add_product_to_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    product = Product("Техника", "Ноутбук", 30000.39, 10)
    category.add_product(product)
    products = category.get_products()
    assert len(products) == 1
    assert "Техника" in products[0]
    assert Category.product_count == 1

    assert product.quantity == 10

    product2 = Product("Смартфон", "iPhone 14", 90000.0, 5)
    category.add_product(product2)
    products = category.get_products()
    assert len(products) == 2
    assert "Смартфон" in products[1]
    assert Category.product_count == 2

    assert product2.quantity == 5


def test_product_price_setter():
    product = Product("Техника", "Ноутбук", 30000.39, 10)

    product.price = 25000.0
    assert product.price == 25000.0

    try:
        product.price = -100
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"

    try:
        product.price = 0
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"

    product.description = "Обновленный ноутбук"
    assert product.description == "Обновленный ноутбук"


def test_product_creation_with_class_method():
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(product_data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    product.quantity = 10
    assert product.quantity == 10


def test_category_product_count():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    product1 = Product("Техника", "Ноутбук", 30000.39, 10)
    product2 = Product("Смартфон", "iPhone 14", 90000.0, 5)

    category.add_product(product1)
    category.add_product(product2)

    assert Category.product_count == 2

    products = category.get_products()
    assert "Техника" in products[0]
    assert "Смартфон" in products[1]


def test_category_multiple_products():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    product1 = Product("Техника", "Ноутбук", 30000.39, 10)
    product2 = Product("Смартфон", "iPhone 14", 90000.0, 5)
    product3 = Product("Планшет", "iPad", 50000.0, 3)

    category.add_product(product1)
    category.add_product(product2)
    category.add_product(product3)
    assert Category.product_count == 3

    products = category.get_products()
    assert len(products) == 3
    assert "Техника" in products[0]
    assert "Смартфон" in products[1]
    assert "Планшет" in products[2]


def test_product_initialization_with_invalid_data():
    try:
        Product("Техника", "Ноутбук", -100, 10)
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"

    try:
        Product("Техника", "Ноутбук", 0, 10)
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"


def test_product_quantity_setter():
    product = Product("Техника", "Ноутбук", 30000.39, 10)

    product.quantity = 15
    assert product.quantity == 15

    try:
        product.quantity = -5
    except ValueError as e:
        assert str(e) == "Количество не может быть отрицательным"

    product.quantity = 0
    assert product.quantity == 0


def test_category_initialization_with_invalid_data():
    try:
        Category("", "Электрические приборы")
    except ValueError as e:
        assert str(e) == "Название категории не может быть пустым"

    try:
        Category("Электроника", "")
    except ValueError as e:
        assert str(e) == "Описание категории не может быть пустым"


if __name__ == "__main__":
    test_create_category()
    test_add_product_to_category()
    test_product_price_setter()
    test_product_creation_with_class_method()
    test_category_product_count()
    test_category_multiple_products()
    test_product_initialization_with_invalid_data()
    test_product_quantity_setter()
    test_category_initialization_with_invalid_data()
    print("Все тесты пройдены!")
