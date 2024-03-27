### Task 1 - Web Scraping 101 (Quotes2Scrape)
# Collect the first 5 quotes (with author) from [quotes.toscrape](https://quotes.toscrape.com/), and store them in a pure text file.

from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

# quotes = [f'"{quote.select_one(".text").get_text(strip=True)}" - {quote.select_one(".author").get_text(strip=True)}'
#           for quote in doc.select('.quote')[:5]]

# for quote in quotes:
#     print(quote)

tbody = doc.tbody
print(tbody)

response = requests.get(url)
print(response.status_code)