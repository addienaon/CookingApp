from bs4 import BeautifulSoup
import requests
from scrapfun import get_ingredients, get_urlpack
import pandas as pd

# for i in range(len(url_list)):
#     print(url_list[i])
#     print(get_ingredients(url_list[i]))

url='https://www.cookwithmanali.com/spinach-dal/#wprm-recipe-container-35643'

def get_html(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    html = doc.find(class_="wprm-recipe wprm-recipe-template-cwm")
    print(html.prettify())

get_html(url)