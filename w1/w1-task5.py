import requests
from lxml import html
import json

# Step 2: Send HTTP Request
url = "https://www.goodreads.com/book/show/4671.To_Kill_a_Mockingbird"
response = requests.get(url)

# Step 3: Parse HTML Content with lxml
tree = html.fromstring(response.content)

# Step 4: Extract Genre Information
genres = []

# Assuming genres are within <a> tags with class 'Button--tag-inline'
genre_links = tree.xpath('//a[contains(@class, "Button--tag-inline")]/span[@class="Button__labelItem"]')
genres = [genre.text.strip() for genre in genre_links]

# Step 5: Write to JSON
genre_data = {'genres': genres}

# Save the data to a JSON file
with open('genre_data.json', 'w') as json_file:
    json.dump(genre_data, json_file, indent=2)

print("Genre information extracted and saved to 'genre_data.json'.")
