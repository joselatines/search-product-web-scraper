from classes.ScrapperFactory import ScrapperFactory
from pprint import pprint


def start_app():
    while True:
        try:
            product_to_search = str(input("🔎 Search the product you want to buy: "))
            results_to_see = int(
                input("❓ How many results you want to see? (default 10): ") or 10
            )

            if results_to_see > 50:
                print("👀 The max is 50 elements")

        except ValueError:
            print("😠 Insert a valid value")

        print("🤔 Searching, please wait...")
        scrapper = ScrapperFactory()

        scrapper.create_ebay_scrapper()
        scrapper.search_all(product_to_search, results_to_see)

        exit_app = str(input("😉 Search again? y/n")).lower() or "y"

        if "n" in exit_app:
            break
