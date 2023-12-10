import random
from create_dummy_data.generate_raw.generate_name import get_name
file = open('sql/client.sql', 'w')

N = 1000

client_type_list = [
    'admin',
    'player',
    'director',
    'owner',
    'general_user',
]

for i in range(1,N+1):
    file.write(f"insert into client (name, password, team_id, client_type) values ('{get_name()}', '{get_name()}', {random.randint(1,10)}, '{random.choice(client_type_list)}');\n")

# user_for_login
file.write(f"insert into client (name, password, team_id, client_type) values ('admin', 'admin', {random.randint(1,10)}, 'admin');\n")
file.write(f"insert into client (name, password, team_id, client_type) values ('player', 'player', {random.randint(1,10)}, 'player');\n")
file.write(f"insert into client (name, password, team_id, client_type) values ('director', 'director', {random.randint(1,10)}, 'director');\n")
file.write(f"insert into client (name, password, team_id, client_type) values ('owner', 'owner', {random.randint(1,10)}, 'owner');\n")
file.write(f"insert into client (name, password, team_id, client_type) values ('general_user', 'general_user', {random.randint(1,10)}, 'general_user');\n")

