import requests

def my_request(endpoint):
    url = f"https://api.chucknorris.io/{endpoint}"
    response = requests.get(url)
    return response.status_code

endpoints = [
    "jokes/random",              
    "jokes/categories",                
    "random",                    
    "jokes/search?query=movie",  
    "jokes/jokes1/"        
]

status_code_meanings = {200: "OK, Successful", 404: "Not Found", 500: "Internal Server Error, "}

def Output_Md(my_request, endpoints, status_code_meanings):
    with open("ChuckNorrisAPI_StatusCodes.md", "w") as md_file:
        md_file.write("# Chuck Norris Jokes API - Status Codes\n\n")
        for endpoint in endpoints:
            status_code = my_request(endpoint)
            status_meaning = status_code_meanings.get(status_code, "Unknown")
        
            md_file.write(f"## Endpoint: /{endpoint}\n\n")
            md_file.write(f"- **Status Code**: {status_code} - {status_meaning}\n")

Output_Md(my_request, endpoints, status_code_meanings)


# i went to HTTpie and tested like that :
# 1st url = https://api.chucknorris.io/jokes/random

# 2nd = https://api.chucknorris.io/jokes/categories

# 3rd = https://api.chucknorris.io/random

# 4th = https://api.chucknorris.io/jokes/search?query=movie

# 5th = https://api.chucknorris.io/jokes/jokes1/


# the output is the same in the file ChuckNorrisAPI_StatusCodes.md
