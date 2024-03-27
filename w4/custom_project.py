from bs4 import BeautifulSoup
import requests

def scrape_recipes(page_num):

    url = f"https://pinchofyum.com/recipes/all/page/{page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    recipes = {}
    recipe_cards = soup.find_all("a", class_="block md:hover:opacity-60 space-y-2")
    
    for card in recipe_cards:
        title = card.find("h3", class_="font-domaine text-2xl normal-case tracking-normal leading-tighter text-black").text.strip()
        ratings_list = []
        average_ratings = soup.find_all(class_=['text-gray-700'])
        for rating in average_ratings:
            if 'average' in rating.get_text():
                ratings_list.append(rating.get_text())
        recipes[title] = rating
        float_ratings_tuple = tuple(float(item.split()[-2]) for item in ratings_list)

    print(float_ratings_tuple)

    # print(recipes)

scrape_recipes(20)
