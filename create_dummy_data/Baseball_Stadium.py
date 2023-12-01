import random
from create_dummy_data.generate_raw.generate_name import get_name
file = open('sql/baseball_stadium.sql', 'w')

for i in range(1, 300):
    location = get_name()
    area = random.randint(10000,1000000)
    capacity = random.randint(2000,100000)
    file.write(f"insert into baseball_stadium (location, area, capacity) values ('{location}', {area}, {capacity});\n")
