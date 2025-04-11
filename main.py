from src.utils import Product, Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    for product_info in category1.get_products():
        print(product_info)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    for product_info in category1.get_products():
        print(product_info)

    print(category1.product_count)

    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(new_product_data)
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    try:
        new_product.price = -100
    except ValueError as e:
        print(e)

    new_product.price = 0
    print(new_product.price)
