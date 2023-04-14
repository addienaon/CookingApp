import os 

postgressql = {'pguser':os.environ['PGUSER'],
                'pgpass':os.environ['PGPASS'],
                'pghost':'localhost',
                'pgport': 5432,
                'pgdb':'recipes',
                }
