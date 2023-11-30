from datetime import datetime
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date

file = open('sql/player_agent.sql', 'w')

start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 12, 1)


for i in range(1,300):
    team_id = random.randint(1,10)
    player_id = random.randint(team_id*10-9, team_id*10)
    sd = generate_random_date(start_date, end_date)
    ed = generate_random_date(start_date, end_date)
    if sd > ed :
        sd, ed = ed, sd
    file.write(f"insert into player_record values ('{i}', '{player_id}', '{sd}', '{ed}', '{team_id}')\n")
