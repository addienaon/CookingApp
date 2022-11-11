from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cookwithmanali.com/honey-cashew-tofu/#wprm-recipe-container-41432"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

name = doc.h1.string #recipee name
amount = doc.find_all(class_="wprm-recipe-ingredient-amount") #ingredient quantity
unit = doc.find_all(class_="wprm-recipe-ingredient-unit") #ingredient unit of measure
ingredients = doc.find_all(class_="wprm-recipe-ingredient-name") #ingredient name

# print(name)
# for i in range(len(ingredients)):
#     print(amount[i].text, unit[i].text, ingredients[i].text)

recipee = {'name':name,
           'amount':amount,
           'unit':unit,
           'ingredients':ingredients}

df = pd.DataFrame(recipee)
print(df)
#df['amount'] = df['amount'].astype(str)