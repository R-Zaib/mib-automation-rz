### Task 2 - Amazon (Kindle Products)
# Collect all the product names, ratings, and prices from this page: <https://www.amazon.com/s?k=kindle>

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.amazon.com/s?k=kindle"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

product_info = []

for item in doc.select('.s-result-item'):
    name = item.select_one('.a-text-normal').get_text(strip=True)
    
    # Some products may not have ratings or prices, so use .find() with specific classes
    rating = item.select_one('.a-icon-star-small .a-icon-alt') if item.select_one('.a-icon-star-small .a-icon-alt') else "N/A"
    price = item.select_one('.a-offscreen') if item.select_one('.a-offscreen') else "N/A"
    
    product_info.append({
        "name": name,
        "rating": str(rating).split(' ')[0] if rating else "N/A",
        "price": price.get_text(strip=True) if price else "N/A"
    })

# Write product information to a JSON file
with open('amazon_products.json', 'w', encoding='utf-8') as file:
    json.dump(product_info, file, ensure_ascii=False, indent=2)

print('Product information saved to amazon_products.json')