from datetime import datetime, timedelta
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date
from create_dummy_data.parser.parse_player_sql import parse_team_id_from_player_sql, parse_player_id_from_player_sql, parse_birth_from_player_sql, parse_from_player_sql
file = open('sql/player_agent.sql', 'w')

start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 12, 1)


for i in range(1,300):
    file_path = 'sql/player.sql'
    player_name = 'player#' + str(random.randint(1,100))
    query = parse_from_player_sql(player_name, file_path)
    team_id = parse_team_id_from_player_sql(query)
    player_id = parse_player_id_from_player_sql(query)

    player_birth = parse_birth_from_player_sql(query)
    player_birth_plus_15_years = player_birth + timedelta(days=365 * 15)

    date = []
    for _ in range(6):
        date.append(generate_random_date(player_birth_plus_15_years, datetime.now().date()))
    date = sorted(date)
    file.write(f"insert into player_record values ('{i}', '{player_id}', '{date[0]}', '{date[1]}', '{team_id}')\n")
    file.write(f"insert into player_record values ('{i}', '{player_id}', '{date[2]}', '{date[3]}', '{team_id}')\n")
    file.write(f"insert into player_record values ('{i}', '{player_id}', '{date[4]}', '{date[5]}', '{team_id}')\n")
    file.write(f"insert into player_record values ('{i}', '{player_id}', '{date[4]}', '{date[5]}', '{team_id}')\n")
