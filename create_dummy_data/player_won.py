import random

file = open('sql/player_won.sql', 'w')

for i in range(1, 101):
    player_id = random.randint(1,100)
    awards_id = random.randint(1,100)
    file.write(f"insert into player_won (player_id, awards_id) values ({player_id}, {awards_id});\n")

