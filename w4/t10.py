"""
    ### Task 10 - E-commerce (Etsy Handmade Jewelry)
    Scrape information about handmade jewelry products on Etsy. Collect details like product name, price, and seller information.    
"""


from bs4 import BeautifulSoup
import requests

url = "https://www.etsy.com/search/jewelry-and-accessories?q=jewelry&order=most_relevant&ref=auto-1&explicit_scope=1"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# tbody = doc.tbody
# print(tbody)
