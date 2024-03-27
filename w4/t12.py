"""
    ### Task 12 - Social Media (Twitter Trending Hashtags)
    Scrape the current trending hashtags on Twitter and store them in a text file. Include the hashtag, number of tweets, and a brief description.
"""

from bs4 import BeautifulSoup
import requests


url = "https://twitter.com/explore"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.content, "html.parser")

if result.status_code == 200:
    trends_div = doc.find_all("div", class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0") # dummy class data based on how twitter uses its classes

    with open("trending_hashtags.txt", "w") as file:
        for trend in trends_div:
            hashtag = trend.find("span", class_="css-901oao css-16my406 r-1qd0xha r-1jouc9e r-9qu9m4 r-o7ynqc r-6416eg").text
            tweet_count = trend.find("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").text
            description = trend.find("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0").next_sibling.text
            
            file.write(f"Hashtag: {hashtag}\n")
            file.write(f"Number of tweets: {tweet_count}\n")
            file.write(f"Description: {description}\n\n")
            
    print("Trending hashtags saved to trending_hashtags.txt")
else:
    print("Failed to fetch data from Twitter")

# due to not finding the correct divs using inpection, there are no hashtags saved in file
# its the process that works
