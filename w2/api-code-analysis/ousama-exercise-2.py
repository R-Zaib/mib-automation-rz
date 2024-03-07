# choose any public api
# try to get as many different http status codes as you can
# document everything in an .md file so that they can be reproduced
# zip any code and the .md and upload the archive to this channel by 18:45 CET

import requests

url ='https://api.thecatapi.com/v1'

def make_request(url):
    response = requests.get(url)
    print(response.status_code)

url1= url + "/images/search"
make_request(url1)

url2 = url + "/imges"
make_request(url2)

url3 = url + "/images/unknown"
make_request(url3)