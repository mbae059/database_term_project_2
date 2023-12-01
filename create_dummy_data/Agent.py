import random
from create_dummy_data.generate_raw.generate_name import get_name
from create_dummy_data.generate_raw.generate_phone_number import get_phone_number
file = open('sql/agent.sql', 'w')


N = 100

for i in range(N):
    file.write(f"insert into agent (agent_name, age, contact_info) values ('{get_name()}', {random.randint(20,60)}, '{get_phone_number()}');\n")
