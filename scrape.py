from bs4 import BeautifulSoup
import requests
from scrapfun import get_ingredients, get_urlpack, get_html
import pandas as pd

# for i in range(len(url_list)):
#     print(url_list[i])
#     print(get_ingredients(url_list[i]))

url='https://www.cookwithmanali.com/spinach-dal/#wprm-recipe-container-35643'

html = get_html(url)
#print(get_ingredients(html))
print(html)