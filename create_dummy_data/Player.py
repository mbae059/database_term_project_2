from datetime import datetime
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date

file = open('sql/player.sql', 'w')

j = 1
cnt = 0
start_date = datetime(1990, 1, 1)
end_date = datetime(2003, 12, 31)


for i in range(1, 11):
    j = (i-1) * 10 + 1
    uniform_number = set()
    while len(uniform_number)<10:
        uniform_number.add(random.randint(1,99))
    li = list(uniform_number)
    file.write(f"insert into player values ('{j+0}', 'player#{j+0}', 'team#{i}', '{i}', 'P', '{li[0]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '1')\n")
    file.write(f"insert into player values ('{j+1}', 'player#{j+1}', 'team#{i}', '{i}','C', '{li[1]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '2')\n")
    file.write(f"insert into player values ('{j+2}', 'player#{j+2}', 'team#{i}', '{i}', '1B', '{li[2]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '3')\n")
    file.write(f"insert into player values ('{j+3}', 'player#{j+3}', 'team#{i}', '{i}', '2B', '{li[3]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '4')\n")
    file.write(f"insert into player values ('{j+4}', 'player#{j+4}', 'team#{i}', '{i}', 'SS', '{li[4]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '5')\n")
    file.write(f"insert into player values ('{j+5}', 'player#{j+5}', 'team#{i}', '{i}', '3B', '{li[5]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '6')\n")
    file.write(f"insert into player values ('{j+6}', 'player#{j+6}', 'team#{i}', '{i}', 'LF', '{li[6]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '7')\n")
    file.write(f"insert into player values ('{j+7}', 'player#{j+7}', 'team#{i}', '{i}', 'CF', '{li[7]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '8')\n")
    file.write(f"insert into player values ('{j+8}', 'player#{j+8}', 'team#{i}', '{i}', 'RF', '{li[8]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '9')\n")
    file.write(f"insert into player values ('{j+9}', 'player#{j+9}', 'team#{i}', '{i}', 'DH', '{li[9]}', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '10')\n")
