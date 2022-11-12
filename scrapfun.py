from bs4 import BeautifulSoup
import requests
import pandas as pd

def ingredient_count(url):
    #get number of ingredients in recipee by passing recipee url.
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    list = doc.find_all('ul',class_="wprm-recipe-ingredients")

    count = 0
    for ul in list:
        for li in ul:
            count += 1
    return(count)

def get_ingredients(url, count):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    df = pd.DataFrame(columns=['amount', 'unit', 'ingredient'])
    if doc.find(class_="wprm-recipe-container"):
        for i in range(count):
            list = doc.find_all('li', class_="wprm-recipe-ingredient")[i]
            if list.find(class_="wprm-recipe-ingredient-amount"):
                amount = list.find(class_="wprm-recipe-ingredient-amount").text
            else: amount=''
            if list.find(class_="wprm-recipe-ingredient-unit"):
                unit = list.find(class_="wprm-recipe-ingredient-unit").text
            else: unit=''
            ingredient = list.find(class_="wprm-recipe-ingredient-name").text
            new_row = pd.Series({'amount':amount, 'unit':unit, 'ingredient':ingredient})
            df = pd.concat([df, new_row.to_frame().T], axis=0, ignore_index=True)
    else: print('RECIPEE CONTAINER DNE')
    return(df)

def get_urls(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    list = doc.find_all('article', class_="article-thumb article-facet")
    count = 0
    ref_list = []
    for article in list:
        count += 1
    for i in range(count):
        refs = doc.find_all('article', class_="article-thumb article-facet")[i].find('a', href=True)
        ref_list.append(refs['href'])
    return(ref_list)

def get_urlpack():
    pack = []
    url = "https://www.cookwithmanali.com/recipes/?_paged=1"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    i = 1
    while doc.find('article', class_="article-thumb article-facet"):
        pack += get_urls(url)
        i += 1
        url = "https://www.cookwithmanali.com/recipes/?_paged={}".format(i)
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
    return(pack)

