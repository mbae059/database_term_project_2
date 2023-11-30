import random

file = open('sql/team_award.sql', 'w')

for i in range(1, 20):
    awards_id = random.randint(1,100)
    year = random.randint(2015,2023)
    team_id = random.randint(1,10)
    file.write(f"insert into awards values ('{i}', '{awards_id}', '{year}', '{team_id}')\n")
