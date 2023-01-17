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

def unit_word_mapper(text):
    from map import unit_dict
    meas_namelok = {'pinch':0, 'inch':1, 'oz':2, 'tsp':3, 'tsps':4, 'tbsp':5, 'tbsp+':6, 'cup':7, 'cups+':8}
    meas_numlok = {0:'pinch', 1:'inch', 2:'oz', 3:'tsp', 4:'tsps', 5:'tbsp', 6:'tbsp+', 7:'cup', 8:'cups+'}
    line_sp = list(text.split(' '))
    line = [i for i in line_sp if i != '']
    return_line_ct = []
    plus = 0
    meas = 'None'
    if len(line)==1:
        # print('len(line): ,' len(line))
        try:
            meas = unit_dict[line[-1]]
        except: meas = text
    elif len(line)>1:
        for i in line:
            # print(i)
            if i=='&': 
                line.remove('&')     
                # print('removing &')
            else:
                i = i.lower()
                if ("+" in i):
                    # print('plus found')
                    plus = 1
                    if (len(i)>1): 
                        i_list = i.split('+')
                        i = "".join(i_list)
                elif any(chr.isdigit() for chr in i): 
                    # print('skip digit')
                    pass
                elif i == '-': pass
                if i in unit_dict:
                    lokup = unit_dict[i]
                    to_list = meas_namelok[lokup]
                    return_line_ct.append(to_list)
                    # print('type found: ', return_line_ct)
        if len(return_line_ct)>1:
            return_line_ct.sort()
            # print(return_line_ct)
            a = return_line_ct[-1]
            b = return_line_ct[-1+1]
            if (plus > 0) & (len(return_line_ct) > 1):
                if (a == b) & (a in [3, 5, 7]):
                    meas = meas_numlok[(a+1)]
                elif (a in [5, 7]):
                    meas = meas_numlok[(a+1)]
                else: meas = meas_numlok[a]
        elif (len(return_line_ct) == 1):
            try: 
                meas = meas_numlok[return_line_ct[-1]] 
            except: pass
        # elif (plus == 0) & (len(return_line_ct) > 1): 
        elif (plus == 0):
            try:
                meas = unit_dict[text]
            except: meas = text
    elif (meas =='None'): 
        try:
            meas = unit_dict[text]
        except: 
            meas = text

    return meas

def ingredient_map(name):
    from map import ingredient_dict
    if name in ingredient_dict:
        name_todb = ingredient_dict[name]
    else: name_todb = name
    return name_todb

def get_ingredients(html):
    list = html.find_all('ul',class_="wprm-recipe-ingredients")
    df = pd.DataFrame(columns=['amount', 'unit', 'ingredient'])
    count = 0
    for ul in list:
        for li in ul:
            count += 1
    i=0
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

def fraction_to_float(amount):
    if ('/') in list(amount.strip()):   
        amount = amount.split('/')
        dec_amount = float(amount[0])/float(amount[1])
    else: dec_amount = float(amount)
    return dec_amount

def add_at_space(amount):
    list_amount = list(amount.strip())
    if ((' ') in list_amount) and (len(list_amount)>3):
        add_amount = amount.split(' ',1)
        left_add = fraction_to_float(add_amount[0])
        right_add = fraction_to_float(add_amount[1])
    elif (('-') in list_amount) and (len(list_amount)>3):
        add_amount = amount.split('-',1)
        left_add = fraction_to_float(add_amount[0])
        right_add = fraction_to_float(add_amount[1])
    
    if len(list_amount)==3:
        left_add = float(list_amount[2])
        right_add = 0
    return (left_add + right_add)

def num_amount(amount):
    if not(type(amount) == list):
        amount_ls = list(amount.strip())
    if '&' in amount_ls:
        amount = amount.replace(' & ', '-')
        amount = amount.replace('&','-')
        amount_ls = list(amount.strip())
    if '+' in amount_ls:
        amount = amount.replace(' + ', '-')
        amount = amount.replace('+ ', '-')
        amount_ls = list(amount.strip())
    if 'to' in amount:
        amount = amount.replace(' to ', '-')
        amount = amount.replace(' to', '')
        amount_ls = list(amount.strip())
    if 'and' in amount:
        amount = amount.replace(' and ', '-')
        amount_ls = list(amount.strip())
    if ' â€“ ' in amount or ' - ' in amount:
        amount = amount.replace(' â€“ ', '-')
        amount = amount.replace(' - ', '-')
        amount_ls = list(amount.strip())
    if ' ' in amount_ls or '-' in amount_ls:
        amount = add_at_space(amount)
    elif (not(' ' in amount_ls or '-' in amount_ls)) and (('/') in amount_ls):
        amount = fraction_to_float(amount)
    elif not(amount_ls == []):
        amount = float(amount)
    else: amount = None
    return amount

def breakup_ingredients(combo_ingredients):
    from map import ingredient_dict
    ingredients_ls = list(combo_ingredients.split(','))
    ls = []
    for i in range(len(ingredients_ls)):
        ing = ingredients_ls[i].strip()
        if ing in ingredient_dict:
            mapped_ing = ingredient_dict[ing]
        else: mapped_ing = ing
        ls.append(mapped_ing)
    return ls
