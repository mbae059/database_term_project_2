from datetime import datetime
import random
from generate_name import get_name
from generate_phone_number import get_phone_number
file = open('./agent.sql', 'w')


N = 100

for i in range(N):
    file.write(f"insert into agent values ('{i+1}', '{get_name()}', '{random.randint(20,60)}', '{get_phone_number()}')\n")
