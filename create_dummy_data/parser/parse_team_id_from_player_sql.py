def parse_team_id_from_player_sql(player_name, file_path=None):
    if file_path is None:
        file_path = '../sql/player.sql'
    file = open(file_path, 'r')
    for line in file:
        if player_name in line:
            query = line.strip()
            team_id = int(query.split(",")[3].strip().strip("'"))
            return team_id
    return None

# Extracting the date string from the query
# Parsing the date string

if __name__ == "__main__":
    player_name = 'player#71'
    print(parse_team_id_from_player_sql(player_name))