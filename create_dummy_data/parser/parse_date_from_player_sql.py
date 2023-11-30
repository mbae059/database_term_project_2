from datetime import datetime

insert_query = "insert into player values ('77', 'player#77', 'team#8', '8', 'LF', '81', '1994-07-26', '28', '7')"
def parse_date_from_player_sql(player_name, file_path=None):
    if file_path is None:
        file_path = '../sql/player.sql'
    file = open(file_path, 'r')
    for line in file:
        if player_name in line:
            query = line.strip()
            date_string = query.split(",")[6].strip().strip("'")
            date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
            return date_object
    return None

# Extracting the date string from the query
# Parsing the date string

if __name__ == "__main__":
    player_name = 'player#76'
    print(parse_date_from_player_sql(player_name))