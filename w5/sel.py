from selenium import webdriver

url = "https://www.imdb.com/"
driver = webdriver.Chrome()
driver.get(url)
search = driver.find_element(by = id, value = "suggestion-search")
print("get search", search.text)