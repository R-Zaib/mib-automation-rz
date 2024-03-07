# List of Giphy API status codes

## 200 - Success
Example of how to successfully invoke the API  

```
api_key = '' #add a valid Giphy API Key.
limit= 6
search_term='' #Add search term
response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips")
print(response.status_code)

```

## 401 Unauthorized
### No API key found in request
In this example the API key is removed from the URL.  

```
api_key = '' #add a valid Giphy API Key.
limit= 6
search_term='' #Add search term
response = requests.get(f"https://api.giphy.com/v1/gifs/search?q={search_term}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips")
print(response.text)
print(response.raise_for_status())

```
## 403 Forbidden
### BANNED
In this example request lacks valid authentication credentials for the target resource, due to expired API key

```
api_key = 'dc6zaTOxFJmzC' #Invalid Giphy API Key.
limit= 6
search_term='' #Add search term
response = requests.get(f"https://api.giphy.com/v1/gifs/search?q={search_term}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips")
print(response.text)
print(response.raise_for_status())

```

## 404 Not found
### Not Found for url
In this example the url is not correctly give eg. there is a typo in the "search" term

```
api_key = '' #add a valid Giphy API Key
limit=6
search_term="sweets"
response = requests.get(f"https://api.giphy.com/v1/gifs/ssearch?api_key={api_key}&q={search_term}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips")
print(response.raise_for_status())

```

## 414 Url too long 
### Client Error
In this example request the length of the search query exceeds 50 characters.

```
api_key = '' #add a valid Giphy API Key
limit=6
search_term="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaavvvvvvvaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&limit={limit}&offset=0&rating=g&lang=en&bundle=messaging_non_clips&q={search_term}")
print(response.text)
print(response.raise_for_status())

```