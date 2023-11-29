from datetime import datetime
import random
from random_date import generate_random_date

file = open('./player.sql', 'w')

j = 1
cnt = 0
start_date = datetime(1990, 1, 1)
end_date = datetime(2003, 12, 31)

#TODO insert uniform_number
for i in range(1, 11):
    j = (i-1) * 10 + 1
    file.write(f"insert into player values ('player#{j+0}', 'team#{i}', 'i', 'P', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '1')\n")
    file.write(f"insert into player values ('player#{j+1}', 'team#{i}', 'i', 'C', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '2')\n")
    file.write(f"insert into player values ('player#{j+2}', 'team#{i}', 'i', '1B', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '3')\n")
    file.write(f"insert into player values ('player#{j+3}', 'team#{i}', 'i', '2B', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '4')\n")
    file.write(f"insert into player values ('player#{j+4}', 'team#{i}', 'i', 'SS', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '5')\n")
    file.write(f"insert into player values ('player#{j+5}', 'team#{i}', 'i', '3B', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '6')\n")
    file.write(f"insert into player values ('player#{j+6}', 'team#{i}', 'i', 'LF', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '7')\n")
    file.write(f"insert into player values ('player#{j+7}', 'team#{i}', 'i', 'CF', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '8')\n")
    file.write(f"insert into player values ('player#{j+8}', 'team#{i}', 'i', 'RF', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '9')\n")
    file.write(f"insert into player values ('player#{j+9}', 'team#{i}', 'i', 'DH', '{generate_random_date(start_date, end_date)}', '{random.randint(1, 100)}', '10')\n")
