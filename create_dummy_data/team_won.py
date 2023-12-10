import random

file = open('sql/team_won.sql', 'w')

for i in range(1, 101):
    team_id = random.randint(1,10)
    awards_id = random.randint(1,100)
    file.write(f"insert into team_won (team_id, awards_id) values ({team_id}, {awards_id});\n")

