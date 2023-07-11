from classes.Scrappers.AmazonScrapper import AmazonScrapper
from classes.Scrappers.EbayScrapper import EbayScrapper
from make_table import make_table
from classes.Products.Product import Product


class ScrapperFactory:
    ebay = {"website": "https://www.ebay.co.uk/sch/"}
    amazon = {
        "website": "https://www.amazon.com/s?k=",
        "headers": {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        },
    }
    EbayScrapper = None
    AmazonScrapper = None

    def create_amazon_scrapper(self):
        self.AmazonScrapper = AmazonScrapper(
            self.amazon["website"], self.amazon["headers"]
        )

        return self.AmazonScrapper

    def create_ebay_scrapper(self):
        self.EbayScrapper = EbayScrapper(self.ebay["website"])

    def search_all(self, product: str, results_to_show=10):
        if results_to_show > 50:
            results_to_show = 50

        ebay_results = self.EbayScrapper.search(product, results_to_show)
        ebay_results_parsed = list(
            map(lambda item: self.parse_data_to_table(item, "Ebay"), ebay_results)
        )

        rows = ebay_results_parsed
        self.show_table(rows)

        return ebay_results

    def parse_data_to_table(self, data: Product, website="Unknown") -> list[str]:
        return [website, data.title, f"${data.price}", data.link]

    def show_table(self, rows):
        columns = ["From", "Title", "Price", "Link"]
        make_table(rows, columns, "Marketplaces results")
