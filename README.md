# Project Description: Recipe Finder
The intention of the web app is to be able to identify which recipees can be made based off of the contents of my fridge/pantry.
The web app is built using Django and PostgreSQL database. An Apache Airflow pipeline is currently being added to check and scrape
manali's website weekly for newly added recipes. 

## Table of Contents
'scrapfun.py': functions used to scrape raw html from my favorite recipee website, [Cook with Manali](https://www.cookwithmanali.com) 
'etl.py', 'models.py', 'map.py': stores the raw data, recipe name, and url in postgreSql. The data is then parsed to identify ingredients, amount, nutrition, cuisine, and units and store them in their respective tables in the db. (see erd below)
'frontend_recipes_finder': Built using django, is a front end editor that allows the user to add/delete items from their fridge & pantry. The ingredients are easily found by searching the appropriate category. A list of recipes is displayed when the recipes tab is selected from the side panel. SQLAlchemy advanced ORM is used to
query the database. 
'pipeline.py': working file, intended to process newly added recipes weekly.

## Entity Relationship Diagram (ERD)
<p align="center">
  <img src="ERD2.png" alt="ERD Diagram">
</p>

