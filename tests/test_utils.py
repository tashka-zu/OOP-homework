from src.utils import Category, Product


def test_create_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    assert category.name == "Электроника"
    assert category.description == "Электрические приборы"
    assert category.products == []
    assert Category.category_count == 1


def test_add_product_to_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Электрические приборы")
    product = Product("Техника", "Ноутбук", 30000.39, 10)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0].name == "Техника"
    assert Category.product_count == 1


def test_category_count():
    Category.category_count = 0
    Category.product_count = 0

    Category("Электроника", "Электрические приборы")
    Category("Мебель", "Домашняя мебель")
    assert Category.category_count == 2
