import pytest

from src.utils import Category, LawnGrass, Product, Smartphone


def test_product_creation():
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_smartphone_creation():
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, 95.0, "Model", "128GB", "Black")
    assert smartphone.name == "Smartphone"
    assert smartphone.description == "Description"
    assert smartphone.price == 500.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.0
    assert smartphone.model == "Model"
    assert smartphone.memory == "128GB"
    assert smartphone.color == "Black"


def test_lawn_grass_creation():
    grass = LawnGrass("Grass", "Description", 50.0, 20, "Country", 10, "Green")
    assert grass.name == "Grass"
    assert grass.description == "Description"
    assert grass.price == 50.0
    assert grass.quantity == 20
    assert grass.country == "Country"
    assert grass.germination_period == 10
    assert grass.color == "Green"


def test_add_same_class_products():
    smartphone1 = Smartphone("Smartphone1", "Description", 500.0, 5, 95.0, "Model1", "128GB", "Black")
    smartphone2 = Smartphone("Smartphone2", "Description", 600.0, 3, 96.0, "Model2", "256GB", "White")
    total_price = smartphone1 + smartphone2
    assert total_price == 500.0 * 5 + 600.0 * 3


def test_add_different_class_products():
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, 95.0, "Model", "128GB", "Black")
    grass = LawnGrass("Grass", "Description", 50.0, 20, "Country", 10, "Green")
    with pytest.raises(TypeError):
        smartphone + grass


def test_category_add_product():
    category = Category("Test Category", "Description")
    smartphone = Smartphone("Smartphone", "Description", 500.0, 5, 95.0, "Model", "128GB", "Black")
    category.add_product(smartphone)
    assert Category.product_count == 1
    assert len(category.get_products()) == 1


def test_category_add_invalid_product():
    category = Category("Test Category", "Description")
    with pytest.raises(TypeError):
        category.add_product("Not a product")
