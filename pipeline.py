from pipeline import DAG,PythonOperator,DummyOperator
from datetime import datetime
from models import Recipe, Ingredient

def scrape_website():
    # Code to scrape website and get recipe name and raw data
    recipe_name = "Example Recipe"
    raw_data = "<html><body><h1>Example Recipe Ingredients:</h1><ul><li>Ingredient 1</li><li>Ingredient 2</li></ul></body></html>"
    return recipe_name, raw_data

def parse_data(recipe_name, raw_data):
    # Code to parse through raw data and add ingredients to database
    # Assumes that a Recipe model and an Ingredient model already exist
    recipe = Recipe.objects.create(name=recipe_name)
    ingredient_list = []
    for ingredient_name in ["Ingredient 1", "Ingredient 2"]:
        ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
        ingredient_list.append(ingredient)
    recipe.ingredients.set(ingredient_list)
    return "Success"

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 15)
}

dag = DAG('example_recipe_pipeline', default_args=default_args, schedule_interval=None)

scrape_task = PythonOperator(
    task_id='scrape_website',
    python_callable=scrape_website,
    dag=dag
)

parse_task = PythonOperator(
    task_id='parse_data',
    python_callable=parse_data,
    op_kwargs={'recipe_name': '{{ task_instance.xcom_pull(task_ids="scrape_website")[0] }}',
               'raw_data': '{{ task_instance.xcom_pull(task_ids="scrape_website")[1] }}'},
    dag=dag
)

dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag
)

scrape_task >> parse_task >> dummy_task
