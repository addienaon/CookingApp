# CookingApp
The cooking app scrapes my favorite recipee website: https://www.cookwithmanali.com and store the raw data, name, and url in postgres sql server. 
The data is then parsed to identify ingredients, amount, and units. The intention of the app is to be able to identify which recipees can be made based off of the 
contents of my fridge/pantry. I have decided to build an ELT pipeline so that I can add aditional information (cook time, prep time, cuisine, etc.) to the database 
without having to re-scrape. 
Project is ongoing, will continue updating.
