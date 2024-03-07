import requests

WEB_URL = "https://api.thedogapi.com/v1"
MY_API_KEY = "live_YdJMqajiRTjZroabKS4cqXftI73koLe963fiHS6HPUSCluGcCFwjob7XzHWu9nho"

def make_request(url, api_key=None):
    headers = {}
    if api_key:
        headers['x-api-key'] = api_key
    
    response = requests.get(url)
    print(f"URL: {url}")
    print(f"Status Code: {response.status_code}")

def upload_image(image_path, api_key=None, sub_id=None):
    url = WEB_URL +"/images/upload"
    headers = {}
    data = {}
    if sub_id:
        data["sub_id"] = sub_id
    if api_key: 
        headers['x-api-key'] = api_key
    files = {"file": open(image_path, "rb")}
    response = requests.post(url, headers=headers, files=files, data=data) 
    return response
    
api_key = MY_API_KEY
my_image_path = "D:\\IBS\\Semester 2\\Automation\\HTTP Status Codes\\pomskey.jpg"
my_sub_id = "pomskeylsy123"


get_code_status_200 = WEB_URL + "/images/search?limit=1"
get_code_status_400 = WEB_URL + "/breeds/weight"
get_code_status_404 = WEB_URL + "/breeeds/"

make_request(get_code_status_200, api_key=MY_API_KEY) 
make_request(get_code_status_400, api_key=MY_API_KEY)
make_request(get_code_status_404, api_key=MY_API_KEY)

upload_response_without_key = upload_image(image_path=my_image_path, sub_id=my_sub_id)
print("Image upload without status code: ", upload_response_without_key.status_code) #401 unauthorized


upload_response_with_key = upload_image(image_path=my_image_path, sub_id=my_sub_id, api_key=MY_API_KEY)
print("image upload with key status code: ",upload_response_with_key.status_code)