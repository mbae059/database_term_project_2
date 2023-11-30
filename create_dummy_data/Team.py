import random

file = open('sql/team.sql', 'w')

for i in range(1,11):
    file.write(f"insert into team values ('{i}', 'team#{i}', '{i}', '{i}', '{random.randint(1950, 2010)}')\n")
