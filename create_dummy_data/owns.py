import random
from create_dummy_data.generate_raw.generate_name import get_name

file = open('sql/owns.sql', 'w')

for i in range(1,11):
    file.write(f"insert into owns (owner_id, team_id) values ({i}, {i});\n")
