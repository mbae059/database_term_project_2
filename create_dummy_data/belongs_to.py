from datetime import datetime, timedelta
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date
from create_dummy_data.parser.parse_player_sql import parse_birth_from_player_sql, parse_from_player_sql
file = open('sql/belongs_to.sql', 'w')

start_date = datetime(2005, 1, 1)
end_date = datetime(2023, 12, 1)


for i in range(1,101):
    file_path = 'sql/player.sql'
    player_id = str(random.randint(1,100))

    player_name = 'player#' + player_id
    # The insert query from player
    query = parse_from_player_sql(player_name, file_path)


    player_birth = parse_birth_from_player_sql(query)

    player_birth_plus_15_years = player_birth + timedelta(days=365 * 15)

    date = []

    first_team_id = random.randint(1,10)
    first_contract_date = generate_random_date(player_birth_plus_15_years, datetime.now().date())
    first_uniform_number = random.randint(1,100)
    first_contract_term = random.randint(1,3)
    first_contract_payment = random.randint(1000,5000)

    second_team_id = (int(player_id)-1) // 10 + 1
    second_contract_date = (datetime.strptime(first_contract_date, '%Y-%m-%d').date() + timedelta(days=365*first_contract_term)).strftime('%Y-%m-%d')
    second_uniform_number = random.randint(1, 100)
    second_contract_term = random.randint(1,3)
    second_contract_payment = random.randint(1000,5000)

    file.write(f"insert into belongs_to (player_id, team_id, start_date, uniform_number, contract_term, contract_payment) values ({player_id}, {first_team_id}, '{first_contract_date}', {first_team_id}, {first_contract_term}, {first_contract_payment});\n")
    file.write(f"insert into belongs_to (player_id, team_id, start_date, uniform_number, contract_term, contract_payment) values ({player_id}, {second_team_id}, '{second_contract_date}', {second_team_id}, {second_contract_term}, {second_contract_payment});\n")
