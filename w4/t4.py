"""
### Task 4 - IMDb (Titanic - Top Actors)
Collect some personal information about the top actors of the Titanic (see Section [Top Cast](https://www.imdb.com/title/tt0120338/?ref_=nv_sr_srsg_0)). The following information should be found:
 - Name
 - Nickname (only one)
 - Height (in meter)
 - Place of Birth
 - Date of Birth (YYYY-MM-DD)
 - Fun Fact
 """

from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/title/tt0120338/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

top_cast_section = doc.find("table", class_="") #unable to find class where top cast is stored

print("Name:", name)
print("Character:", character)

# tbody = doc.tbody
# print(tbody)

# trs = tbody.contents
