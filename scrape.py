from bs4 import BeautifulSoup
import requests
from scrapfun import ingredient_count, get_ingredients, get_urlpack
import pandas as pd

# url = "https://www.cookwithmanali.com/recipes/?_paged=1"

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

pack = get_urlpack()

for u in len(range(pack)):
    count = ingredient_count(u)
    ingredients = get_ingredients(u, count)
    print(u)
    