from classes.Products.Product import Product
import re


class EbayProduct(Product):
    def __init__(
        self,
        title: str,
        price: str,
        seller_feedback_rate: str,
        img_path: str,
        link: str,
        condition: str,
    ):
        super().__init__(title, price, link, condition)
        self.__price = price
        self.__seller_feedback_rate = seller_feedback_rate
        self.__img_path = img_path

    def __str__(self) -> str:
        return f"😀 EbayProduct:  {self.title} { self.price} { self.condition} {self.seller_feedback_rate} {self.__img_path}"

    def __repr__(self) -> str:
        # return f"{self.price}"
        return f"{self.title}, {self.price}, {self.condition}, {self.seller_feedback_rate}, {self.__img_path}"

    @property
    def price(self) -> int:
        property_parsed = self.__price.lower().strip().strip("£").replace(",", ".")
        float_number = re.findall(r"\d+\.\d+", property_parsed)[0]
        property_parsed = int(float(float_number))

        return property_parsed

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def seller_feedback_rate(self):
        property_parsed = self.__seller_feedback_rate.lower()
        return property_parsed
