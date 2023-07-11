from bs4 import BeautifulSoup
import requests

from classes.Products.Product import Product


class Scrapper:
    soup: BeautifulSoup = None

    def __init__(self, website_url, headers={}):
        self.website_url = website_url
        self.headers = headers

    # get base website without managing the data yet
    def request_website(self, product: str) -> BeautifulSoup:
        response = requests.get(f"{self.website_url}{product}", headers=self.headers)

        self.soup = BeautifulSoup(response.text, "html.parser")

        return self.soup

    def scrape_products(self) -> Product:
        html_elements = {
            "parent": {"tag": "div", "class_name": "s-result-list"},
            "title": {
                "tag": "span",
                "class_name": "a-size-medium a-color-base a-text-normal",
            },
            "price": {"tag": "span", "class_name": "a-price-whole"},
            "link": {
                "tag": "a",
                "class_name": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal",
            },
        }

        parent = html_elements["parent"]
        title = html_elements["title"]
        price = html_elements["price"]
        link = html_elements["link"]

        products_html = self.soup.find_all(parent["tag"], class_=parent["class_name"])

        def find_html_elements(item):
            title = item.find(title["tag"], class_=title["class_name"])
            price = item.find(price["tag"], class_=price["class_name"])
            link = item.find(link["tag"], class_=link["class_name"]).get("href")

            return {title, price, link}

        html_element = list(map(find_html_elements, products_html))

        def cb():
            for item in self.soup.find_all(parent["tag"], class_=parent["class_name"]):
                item_title = item.find(title["tag"], class_=title["class_name"])
                item_price = item.find(price["tag"], class_=price["class_name"])
                item_link = item.find(link["tag"], class_=link["class_name"]).get(
                    "href"
                )
