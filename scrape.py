from bs4 import BeautifulSoup
import requests
from scrapfun import ingredient_count, get_ingredients
import pandas as pd
from lxml import html

url = "https://www.cookwithmanali.com/recipes/"
#"https://www.cookwithmanali.com/jackfruit-biryani/#wprm-recipe-container-58953"
#"https://www.cookwithmanali.com/honey-cashew-tofu/#wprm-recipe-container-41432"
#"https://www.cookwithmanali.com/atta-biscuits/"
#"https://www.cookwithmanali.com/paan-mousse/"

#count = ingredient_count(url)
#df = get_ingredients(url, count)
#print(df)

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
list = doc.find_all('article', class_="article-thumb article-facet")
count = 0
for article in list:
    count += 1

for i in range(count):
    pp = doc.find_all('article', class_="article-thumb article-facet")[i].find('a', href=True)
    print(pp['href'])

//*[@id="post-42980"]/div/div[4]/div/a[6]