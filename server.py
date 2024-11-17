from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper.scraper import AmazonScraper

app = Flask(__name__)
CORS(app)  

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json 
    query = data.get("query", "").strip() 
    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        scraper = AmazonScraper()  
        products = scraper.scrape(query)  
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
