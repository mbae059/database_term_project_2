import random

file = open('sql/client.sql', 'w')

N = 1000
for i in range(1,N+1):
    file.write(f"insert into client values ('{i}', 'team#{i}', '{i}', '{i}', '{random.randint(1950, 2010)}')\n")
