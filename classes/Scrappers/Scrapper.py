from bs4 import BeautifulSoup
import requests
from classes.Products.Product import Product


class Scrapper:
    def __init__(self, website_url, headers={}):
        self.website_url = website_url
        self.headers = headers
        self.soup = None

    def request_website(self, product: str) -> BeautifulSoup:
        response = requests.get(f"{self.website_url}{product}", headers=self.headers)
        self.soup = BeautifulSoup(response.text, "html.parser")

        return self.soup

    def scrape_products_testing(self, html_elements) -> Product:
        parent = html_elements["parent"]
        title = html_elements["title"]
        price = html_elements["price"]
        link = html_elements["link"]

        products_html = self.soup.find_all(parent["tag"], class_=parent["class_name"])

        def find_html_elements(item):
            title_elem = item.find(title["tag"], class_=title["class_name"])
            price_elem = item.find(price["tag"], class_=price["class_name"])
            link_elem = item.find(link["tag"], class_=link["class_name"]).get("href")

            return Product(title_elem, price_elem, link_elem)

        html_elements = list(map(find_html_elements, products_html))

        return html_elements
