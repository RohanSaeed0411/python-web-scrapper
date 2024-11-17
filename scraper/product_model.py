from datetime import datetime

class Product:
    def __init__(self, title, total_reviews, price, image_url, query):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_url = image_url
        self.query = query
        self.scrape_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "total_reviews": self.total_reviews,
            "price": self.price,
            "image_url": self.image_url,
            "query": self.query,
            "scrape_date": self.scrape_date
        }
