import random

file = open('sql/baseball_records.sql', 'w')

for i in range(1, 300):
    team1_id = None
    team2_id = None

    while team1_id == team2_id:
        team1_id = random.randint(1,10)
        team2_id = random.randint(1,10)

    baseball_stadium_id = random.randint(1,100)

    team1_score = random.randint(1,10)
    team2_score = random.randint(1,10)

    score = str(team1_score) + ':' + str(team2_score)

    file.write(f"insert into baseball_records values ('{i}', '{team1_id}', '{team2_id}', '{baseball_stadium_id}', '{score}')\n")
