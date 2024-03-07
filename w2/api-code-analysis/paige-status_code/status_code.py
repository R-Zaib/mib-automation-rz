import requests

# status code 200 Okay 
url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
print(response.status_code)

# status code 404 Not Found 
url = "https://swapi.dev/api/people/100/"
response = requests.get(url)
print(response.status_code)

#status code 405 Method Not Allowed
url = "https://swapi.dev/api/people/83/"
response = requests.post(url)
print(response.status_code)

















