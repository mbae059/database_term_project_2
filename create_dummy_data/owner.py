import random
from create_dummy_data.generate_raw.generate_name import get_name

file = open('sql/owner.sql', 'w')

for i in range(1,100):
    file.write(f"insert into owner (name, age, budget) values ('{get_name()}', {random.randint(30,70)}, {random.randint(500,1000)});\n")
