import requests
import time
from bs4 import BeautifulSoup
from .product_model import Product

class AmazonScraper:
    BASE_URL = "https://www.amazon.com/s"
    HEADERS = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' ,'Accept-Language': 'en-US, en;q=0.5'}
    def __init__(self, max_pages=20):
        self.max_pages = max_pages

    def fetch_html(self, query, page):
        try:
            params = {'k': query, 'page': page}
            url = f"{self.BASE_URL}?k={params['k']}&page={params['page']}"
            response = requests.get(url=url, headers=self.HEADERS)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch {url}, status code: {response.status_code}")
                return None
       
        except requests.RequestException as e:
            print(f"Network error: {e}")
            return None

    def parse_page(self, html, query):
        soup = BeautifulSoup(html, 'html.parser')
        product_elements = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        products = []

        for product in product_elements:
            try:
                title = product.h2.text.strip() if product.h2 else "No Title"
                total_reviews = (
                product.find('span', {'class': 'a-size-base'}).text.strip()
                if product.find('span', {'class': 'a-size-base'})
                else "No Reviews"
                )
                price = (
                    product.find('span', {'class': 'a-offscreen'}).text.strip()
                    if product.find('span', {'class': 'a-offscreen'})
                    else "No Price"
                )
                image_url = (
                    product.find('img')['src']
                    if product.find('img') and 'src' in product.find('img').attrs
                    else "No Image"
                )
                products.append(Product(title, total_reviews, price, image_url, query))
            except Exception as e:
                print(f"Error parsing a product element: {e}")

        return products

    def scrape(self, query):
        all_products = []
        for page in range(1, self.max_pages + 1):
            html = self.fetch_html(query, page)
            if html:
                products = self.parse_page(html, query)
                all_products.extend(products)
            time.sleep(2) 
        return all_products
