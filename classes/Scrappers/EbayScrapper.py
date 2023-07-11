from classes.Scrappers.Scrapper import Scrapper
from classes.Products.EbayProduct import EbayProduct


class EbayScrapper(Scrapper):
    def __init__(self, website_url):
        super().__init__(website_url)

    def search(self, product: str, results_to_see=1) -> list[EbayProduct]:
        self.soup = super().request_website(product)

        products = self.scrape_products()

        products_filtered = self.filter_products(products, product, results_to_see)

        return products_filtered

    def filter_products(
        self,
        unfiltered_products: list[EbayProduct],
        product_query: str,
        output_products=1,
    ):
        products_filtered = []

        def filter_by_characteristics(
            unfiltered_products: list[EbayProduct],
        ) -> list[EbayProduct]:
            def only_item_with_points(item):
                # (ProductClass, points)
                if item[1] > 0:
                    return True

            products_points = []
            for product in unfiltered_products:
                points = 0

                # characteristics
                is_new = "brand new".strip() in product.condition
                matched_with_query = product.title in product_query

                if is_new:
                    points += 2

                elif matched_with_query:
                    points += 1

                products_filtered.append((product, points))

            products_points = list(filter(only_item_with_points, products_filtered))

            actual_filtered_products = []
            for product_with_points in products_points:
                actual_filtered_products.append(product_with_points[0])

            return actual_filtered_products

        products_filtered = filter_by_characteristics(unfiltered_products)

        def lowest_price(elem: EbayProduct):
            return elem.price

        products_filtered.sort(key=lowest_price)

        return products_filtered[:output_products]

    def scrape_products(self):
        products = []

        for li in self.soup.find_all("li", class_="s-item"):
            item_title = li.find("div", class_="s-item__title")
            item_price = li.find("span", class_="s-item__price")
            item_condition = li.find("span", class_="SECONDARY_INFO")
            item_link = li.find("a", class_="s-item__link").get("href")
            item_seller_feedback_rate = li.find(
                "span", class_="s-item__seller-info-text"
            )
            item_img_path = (
                li.find("div", class_="s-item__image-wrapper").find("img").get("src")
            )

            emptyValue = any(
                item is None
                for item in [
                    item_title,
                    item_price,
                    item_condition,
                    item_seller_feedback_rate,
                    item_img_path,
                    item_link,
                ]
            )

            if emptyValue:
                continue

            title = item_title.text.strip()
            price = item_price.text.strip()
            condition = item_condition.text.strip()
            seller_feedback_rate = item_seller_feedback_rate.text.strip()
            img_path = item_img_path

            # 🛑 £8.99 to £14.99
            if "to" in price:
                continue

            product = EbayProduct(
                title, price, seller_feedback_rate, img_path, item_link, condition
            )

            products.append(product)

        return products
