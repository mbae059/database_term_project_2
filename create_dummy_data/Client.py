import random
from create_dummy_data.generate_raw.generate_name import get_name
file = open('sql/client.sql', 'w')

N = 1000

client_type_list = [
    'admin',
    'player',
    'director',
    'owner',
    'agent',
    'general_user',
    'GM', #general_manager
    ]
for i in range(1,N+1):
    file.write(f"insert into client values ('{i}', '{get_name()}', '{get_name()}', '{random.randint(1,10)}', '{random.choice(client_type_list)}')\n")

# user_for_login
file.write(f"insert into client values ('{N+1}', 'admin', 'admin', '{random.randint(1,10)}', 'admin')\n")
file.write(f"insert into client values ('{N+2}', 'player', 'player', '{random.randint(1,10)}', 'player')\n")
file.write(f"insert into client values ('{N+3}', 'director', 'director', '{random.randint(1,10)}', 'director')\n")
file.write(f"insert into client values ('{N+4}', 'owner', 'owner', '{random.randint(1,10)}', 'owner')\n")
file.write(f"insert into client values ('{N+5}', 'agent', 'agent', '{random.randint(1,10)}', 'agent')\n")
file.write(f"insert into client values ('{N+6}', 'general_user', 'general_user', '{random.randint(1,10)}', 'general_user')\n")
file.write(f"insert into client values ('{N+7}', 'GM', 'GM', '{random.randint(1,10)}', 'GM')\n")
