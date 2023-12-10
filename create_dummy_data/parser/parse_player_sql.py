import re
from datetime import datetime

def parse_list(query):
    values_match = re.search(r"values \((.*?)\)", query)
    if values_match:
        values_str = values_match.group(1)
        values_list = [value.strip("'") for value in values_str.split(",")]
        values_list = [value.strip().lstrip("'") for value in values_list]
        return values_list
    else:
        return None
def parse_from_player_sql(player_name, file_path=None):
    if file_path is None:
        file_path = '../sql/player.sql'
    file = open(file_path, 'r')
    for line in file:
        if player_name in line:
            query = line.strip()
            return parse_list(query)
    return None

def parse_id_from_player_sql(list_player_sql):
    return int(''.join(filter(str.isdigit, list_player_sql[0])))

def parse_position_from_player_sql(list_player_sql):
    return list_player_sql[1]
def parse_birth_from_player_sql(list_player_sql):
    date_string = list_player_sql[2]
    date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
    return date_object

# Extracting the date string from the query
# Parsing the date string

if __name__ == "__main__":
    # insert_query = "insert into player values ('player#77', 'team#8', 8, 'LF', 81, '1994-07-26', 28, 7)"
    insert_query = "insert into player(name, position, birth) values ('player#33', '1B', '1987-01-23');"
    player_name = 'player#76'
    li = parse_from_player_sql(player_name)
    print(li)
    print(parse_position_from_player_sql(li))
    print(parse_birth_from_player_sql(li))
