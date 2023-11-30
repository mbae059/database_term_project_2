import random

file = open('sql/individual_award.sql', 'w')

for i in range(1, 20):
    awards_id = random.randint(101,200)
    year = random.randint(2015,2023)
    player_id = random.randint(1,100)
    file.write(f"insert into awards values ('{i}', '{awards_id}', '{year}', '{player_id}')\n")
