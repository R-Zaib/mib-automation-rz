# Beautiful Soup

## Materials & Resources

| Material                                                                     |  Time |
| :--------------------------------------------------------------------------- | ----: |
| [What is Web Scraping?](https://www.youtube.com/watch?v=dlj_QL-ENJM)         |  3:24 |
| [What is Robots.txt?](https://www.youtube.com/watch?v=ioULOSwSaBk)         |  2:56 |
| [Beautiful Soup - Intro](https://www.youtube.com/watch?v=aIPqt-OdmS0)         |  9:48 |
| [BeautifulSoup find() and find_all() methods](https://www.youtube.com/watch?v=Fin_f2uqmK4)         |  16:25 |
| [How to get text?](https://www.youtube.com/watch?v=OIs4EYyAcoo)         |  2:07 |
| [WebScrapping With Python urllib BeautifulSoup Regular Expression](https://www.youtube.com/watch?v=_6sp7jF0q54)         |  10:30 |
| [How I Scrape multiple pages on Amazon with Python, Requests & BeautifulSoup](https://www.youtube.com/watch?v=4VfqVpTz4Q4)         |  11:23 |
| [User Agent Switching](https://www.youtube.com/watch?v=90t9WkQbQ2E)         |  6:52 |

| Optional                                                                     |   |
| :--------------------------------------------------------------------------- | ----: |
| [5 Things You Might Not Be Using in BeautifulSoup](https://www.youtube.com/watch?v=3tUUVenpxbc)         |  10:31 |
| [Login To Any Website using Python and Requests](https://www.youtube.com/watch?v=bM50i7sKwwM)         |  8:01 |
| [Ultimate Guide to Web Scraping](https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/)         |  reading |

## Installation
A complet installation guide can be found [here](https://www.youtube.com/watch?v=gcnc1fQ8c84) or you can directly install it via pip:
```
pip install beautifulsoup4
```



## Exercises

### Task 1 - Web Scraping 101 (Quotes2Scrape)
Collect the first 5 quotes (with author) from [quotes.toscrape](https://quotes.toscrape.com/), and store them in a pure text file.

### Task 2 - Amazon (Kindle Products)
Collect all the product names, ratings, and prices from this page: <https://www.amazon.com/s?k=kindle>

### Task 3 - Amazon (Books)
Collect at least 5000 product names, ratings, and prices from the book category

### Task 4 - IMDb (Titanic - Top Actors)
Collect some personal information about the top actors of the Titanic (see Section [Top Cast](https://www.imdb.com/title/tt0120338/?ref_=nv_sr_srsg_0)). The following information should be found:
 - Name
 - Nickname (only one)
 - Height (in meter)
 - Place of Birth
 - Date of Birth (YYYY-MM-DD)
 - Fun Fact

If any of the above information is not found use `N/A` instead.

### Task 5 - Wikipedia (Python Programming Language)
Extract information about the Python programming language from its [Wikipedia page](https://en.wikipedia.org/wiki/Python_(programming_language)). Retrieve details such as:
 - Year of creation
 - Developer(s)
 - Latest stable release version and date
 - Paradigm(s)
 - Typing discipline

### Task 6 - Stack Overflow (Python Questions)
Scrape the titles and links of the top 20 Python-related questions from [Stack Overflow](https://stackoverflow.com/questions/tagged/python) and store them in a text file.

### Task 7 - News Headlines (BBC)
Retrieve the latest news headlines from the BBC News website and store them in a text file. Include the title, publication date, and a brief summary for each headline.

### Task 8 - IMDB (Top 250 Movies)
Scrape the top 10 movies from IMDB's [Top 250 Movies](https://www.imdb.com/chart/top/) list. Extract details such as title, release year, rating, and brief plot summary.

### Task 9 - Job Search (LinkedIn)
Scrape job listings for Python developers on LinkedIn. Extract details like job title, company, location, and the date the job was posted.

### Task 10 - E-commerce (Etsy Handmade Jewelry)
Scrape information about handmade jewelry products on Etsy. Collect details like product name, price, and seller information.

### Task 11 - Wikipedia (List of Presidents)
Extract information about all the presidents of the United States from the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). Retrieve details such as name, birth date, death date, and political party.

### Task 12 - Social Media (Twitter Trending Hashtags)
Scrape the current trending hashtags on Twitter and store them in a text file. Include the hashtag, number of tweets, and a brief description.

### Task 13 - Music (Spotify Top Tracks)
Scrape the current top tracks on Spotify and store them in a text file. Include details like the track title, artist, and popularity score.

### Task 14 - Sports (NBA Player Stats)
Retrieve the current season statistics for NBA players from the [NBA website](https://www.nba.com/stats/players/). Extract details like player name, team, points per game, and assists per game.

### Task 15 - Scientific Publications (IEEE Xplore)
Scrape information about the latest scientific publications in the field of computer science from [IEEE Xplore](https://ieeexplore.ieee.org/). Include details like paper title, authors, publication date, and abstract.

### Task 16 - Real Estate Listings (Zillow)
Scrape real estate listings from Zillow for a specific location. Collect details like property name, price, number of bedrooms, and address.
