import random
from create_dummy_data.generate_raw.generate_name import get_name

file = open('sql/director.sql', 'w')

for i in range(1,11):
    file.write(f"insert into director (director_name, director_year, team_id, income) values ('{get_name()}', '{random.randint(1980,2010)}', {i}, {random.randint(500, 1000)});\n")
