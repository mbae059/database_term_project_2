from create_dummy_data.parser.parse_player_sql import parse_birth_from_player_sql, parse_team_id_from_player_sql, parse_from_player_sql
from generate_raw.generate_random_date import generate_random_date
from datetime import datetime, timedelta
file = open('sql/player_record.sql', 'w')

for i in range(1,101):
    player_name = 'player#' + str(i)
    player_record_date = []
    file_path = 'sql/player.sql'
    query = parse_from_player_sql(player_name, file_path)
    player_birth = parse_birth_from_player_sql(query)
    player_birth_plus_15_years = player_birth + timedelta(days=365 * 15)
    while len(player_record_date)<4:
        player_record_date.append(generate_random_date(player_birth_plus_15_years, datetime.now().date()))

    player_record_date = sorted(player_record_date)
    file.write(f"insert into player_record values ('{2*i-1}', '{i}', '{player_record_date[0]}', '{player_record_date[1]}', '{parse_team_id_from_player_sql(query)}')\n")
    file.write(f"insert into player_record values ('{2*i}', '{i}', '{player_record_date[2]}', '{player_record_date[3]}', '{parse_team_id_from_player_sql(query)}')\n")
