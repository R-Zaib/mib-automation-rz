import requests

#HTTP Code - 200 OK
url = 'https://emojihub.yurace.pro/api/all'
reponse = requests.get(url)
codee = reponse.status_code
print(codee)


#HTTP Code - 404 Not Found
url = 'https://emojihub.yurace.pro/api/only_happy_emoji'
response = requests.get(url)
codee = response.status_code
print(codee)

# HTTP Code - 400 (in postman)
url = 'https://ec.europa.eu/transparency/expert-groups-register/core/api/front/meetings/search?page=0&size=10'
reponse = requests.post(url)
codee = response.status_code
print(codee)


# HTTP Code - 405 Method Not Allowed (in postman)
url = 'https://emojihub.yurace.pro/api/only_happy_emoji'
reponse = requests.post(url)
codee = response.status_code
print(codee)

response = requests.get('https://emojihub.')
print(response)
