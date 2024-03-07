import requests

api_key = 'R6BqA9Dc2zIx8SBjPY5YC98pkTlwm07J' #add valid Giphy API key
limit=6
search_term="sweet"
response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips&q={search_term}")

print(response.text)
print(response.raise_for_status())


