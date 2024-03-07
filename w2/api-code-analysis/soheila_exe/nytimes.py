"""Exchange rate app"""
import logging
import requests

def get_information(url):
    """get information form New york times"""
    response = requests.get(url= url, timeout= 10)
    if response.status_code == 200:
        return "success"
    if response.status_code == 401:
        return "unauthorized, invalid api keys"
    if response.status_code == 404:
        return "invalid url"
def create_logger():
    """create logger"""
    logger = logging.getLogger("__name__")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(message)s %(levelname)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger
def main():
    """set api key and call get_information"""
    api_key = "ecmEGhTeFYvTGEAWcYZ6KJGmW6jrOjy0"
    base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    url = base_url+f"?q=Apollo 11&api-key={api_key}"
    logger = create_logger()
    result = get_information(url)
    logger.info(result)
if __name__ == "__main__":
    main()
