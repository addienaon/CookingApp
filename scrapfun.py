from bs4 import BeautifulSoup
import requests

def ingredient_count(url):
    #get number of ingredients in recipee by passing recipee url.
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    list = doc.find('ul',class_="wprm-recipe-ingredients").find_all('li', class_="wprm-recipe-ingredient")

    count = 0
    for li in list:
        count += 1
    return(count)

def get_ingredients(url, count):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    i=1
    for i in range(count):
        list = doc.find_all('li', class_="wprm-recipe-ingredient")[i]
        if list.find(class_="wprm-recipe-ingredient-amount"):
            amount = list.find(class_="wprm-recipe-ingredient-amount").text
        else: amount=''
        unit = list.find(class_="wprm-recipe-ingredient-unit").text
        ingredient = list.find(class_="wprm-recipe-ingredient-name").text
        print(amount, unit, ingredient)
