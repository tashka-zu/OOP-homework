from src.utils import Product, Category

def test_create_product():
    product = Product("Техника", "Ноутбук", 30000.39, 10)
    assert product.name == "Техника"
    assert product.description == "Ноутбук"
    assert product.price == 30000.39
    assert product.quantity == 10

def test_create_category():
    category = Category("Электроника", "Электрические приборы")
    assert category.name == "Электроника"
    assert category.description == "Электрические приборы"
    assert category.products == []

def test_add_product_to_category():
    category = Category("Электроника", "Электрические приборы")
    product = Product("Техника", "Ноутбук", 30000.39, 10)
    category.products.append(product)
    assert len(category.products) == 1
    assert category.products[0].name == "Техника"

def test_product_attributes():
    product = Product("Кухонные приборы", "Плита", 60000.99, 3)
    assert product.price == 60000.99
    assert product.quantity == 3
    product.price = 50000.99
    product.quantity = 4
    assert product.price == 50000.99
    assert product.quantity == 4
