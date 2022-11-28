from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_html(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    raw_data = doc.find(class_="wprm-recipe wprm-recipe-template-cwm")
    name = doc.find(class_="wprm-recipe-name wprm-block-text-bold").text
    dict = {'name':name, 'url':url, 'data':raw_data}
    row = pd.Series(data=dict)
    return(row)

def get_ingredients(html):
    list = html.find_all('ul',class_="wprm-recipe-ingredients")
    df = pd.DataFrame(columns=['amount', 'unit', 'ingredient'])
    count = 0
    for ul in list:
        for li in ul:
            count += 1
    
    for i in range(count):
        list = html.find_all('li', class_="wprm-recipe-ingredient")[i]
        if list.find(class_="wprm-recipe-ingredient-amount"):
            amount = list.find(class_="wprm-recipe-ingredient-amount").text
        else: amount=''
        if list.find(class_="wprm-recipe-ingredient-unit"):
            unit = list.find(class_="wprm-recipe-ingredient-unit").text
        else: unit=''
        ingredient = list.find(class_="wprm-recipe-ingredient-name").text
        new_row = pd.Series({'amount':amount, 'unit':unit, 'ingredient':ingredient})
        df = pd.concat([df, new_row.to_frame().T], axis=0, ignore_index=True)
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
    with open('url_container_pack.txt', 'r') as filedata:
            url_list = filedata.readlines()
    
    while doc.find('article', class_="article-thumb article-facet"):
        pack += get_urls(url)
        i += 1
        url = "https://www.cookwithmanali.com/recipes/?_paged={}".format(i)
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
    return(pack)

def get_container_pack():
    pack = get_urlpack()
    container_pack = []
    for i in range(len(pack)):
        result = requests.get(pack[i])
        doc = BeautifulSoup(result.text, "html.parser")
        if doc.find(class_="wprm-recipe-container"): 
            container_pack.append(pack[i])

    with open('url_container_pack.txt', 'w') as f:
        for line in container_pack:
            f.write(line)
            f.write('\n')
    return(i) #i: page last scraped

def check_new_url():
    with open('url_container_pack.txt', 'r') as f:
        data = f.readlines()
        data = [data[i].rstrip('\n') for i in range(len(data))]
        f.close()
    pack = []
    url = "https://www.cookwithmanali.com/recipes/?_paged=1"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    if doc.find('article', class_="article-thumb article-facet"):
        pack = get_urls(url)
    lineset = set(data)
    packset = set(pack)
    new_url_ls = packset.difference(lineset)  
    return (new_url_ls)
