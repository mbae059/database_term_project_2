import random
from datetime import datetime

from create_dummy_data.generate_raw.generate_name import get_name
from create_dummy_data.generate_raw.generate_random_date import generate_random_date
file = open('sql/director.sql', 'w')


for i in range(1,100):
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2003, 12, 31)
    date = generate_random_date(start_date, end_date)
    file.write(f"insert into director (name, start_date) values ('{get_name()}', '{date}');\n")
