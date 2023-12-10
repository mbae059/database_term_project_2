import random
from datetime import datetime

from create_dummy_data.generate_raw.generate_random_date import generate_random_date
file = open('sql/directs.sql', 'w')


for i in range(1,11):
    contract_term = random.randint(1,3)
    start_date = generate_random_date(datetime(2003, 12, 31), datetime(2006, 12, 31))


    file.write(f"insert into directs (director_id, team_id, contract_term, start_date, contract_payment) values ({i}, {i}, '{contract_term}', '{start_date}', {random.randint(1000,3000)});\n")
