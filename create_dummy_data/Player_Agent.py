from datetime import datetime, timedelta
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date
from create_dummy_data.parser.parse_player_sql import parse_team_id_from_player_sql, parse_player_id_from_player_sql, parse_birth_from_player_sql, parse_from_player_sql
file = open('sql/player_agent.sql', 'w')

start_date = datetime(2005, 1, 1)
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

    first_contract_date = generate_random_date(player_birth_plus_15_years, datetime.now().date())
    first_contract_term = random.randint(1,3)

    second_contract_date = (datetime.strptime(first_contract_date, '%Y-%m-%d').date() + timedelta(days=365*first_contract_term)).strftime('%Y-%m-%d')
    second_contract_term = random.randint(1,3)

    file.write(f"insert into player_agent (player_id, agent_id, team_id, contract_date, contract_term, contract_payment) values ({i}, {random.randint(1,100)}, {random.randint(1,10)}, '{first_contract_date}', {first_contract_term}, {random.randint(500,1000)});\n")
    file.write(f"insert into player_agent (player_id, agent_id, team_id, contract_date, contract_term, contract_payment) values ({i}, {random.randint(1,100)}, {random.randint(1,10)}, '{second_contract_date}', {second_contract_term}, {random.randint(500,1000)});\n")
