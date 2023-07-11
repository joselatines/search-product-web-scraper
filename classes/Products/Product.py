class Product:
    class_counter = 0

    def __init__(self, title: str, price: str, link: str, condition="unknown"):
        self.price = price
        self.title = title.lower()
        self.link = link
        self.condition = condition.lower()
        self.id = Product.class_counter
        Product.class_counter += 1
