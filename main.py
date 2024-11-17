from scraper.input_reader import read_queries
from scraper.scraper import AmazonScraper
from scraper.output_saver import save_to_json

def main():
    queries = read_queries()
    scraper = AmazonScraper()

    for query in queries:
        print(f"Scraping data for query: {query}")
        products = scraper.scrape(query)
        save_to_json(products, query)

if __name__ == "__main__":
    main()
