import psycopg2


def player(cursor):
    print('create user')
    name = input('player name : ')
    position = input('position : ')
    birth = input('birth : ')
    # create query

    query = f"INSERT INTO players (name, position, birth) VALUES ('{name}', '{position}', '{birth}')"
    cursor.execute(query)


def team(cursor):
    print('create team')
    team_name = input('team name : ')
    owner_ID = input('owner id : ')
    director_ID = input('director id : ')
    establishment_year = input('establishment year : ')


def belongs_to(cursor):
    # todo
    pass


def owner(cursor):
    print('create owner')
    team_id = input('team id : ')
    owner_name = input('owner name : ')
    owner_age = input('owner age : ')
    budget = input('budget : ')


def owns(cursor):
    # todo
    pass


def director(cursor):
    print('create director')
    director_name = input('director name : ')
    director_year = input('director year : ')
    team_id = input('team id : ')
    income = input('income : ')


def directs(cursor):
    print('create director')
    director_name = input('director name : ')
    director_year = input('director year : ')
    team_id = input('team id : ')
    income = input('income : ')


def player_agent(cursor):  # budget 이 예산? 그렇다면 signing bonus...
    print('create player_agent')
    agent_id = input('agent ID : ')
    player_id = input('player ID : ')
    team_id = input('team ID : ')
    contract_date = input('contract date : ')
    contract_term = input('contract term : ')
    signing_bonus = input('signing bonus : ')


def awards(cursor):
    print('create awards name')
    awards_name = input('awards name : ')


def player_won(cursor):
    # todo
    pass


def team_won(cursor):
    # todo
    pass


def client(cursor):
    print('create user')
    user_ID = input('user ID : ')
    user_name = input('user name : ')
    team_id = input('team id : ')
    type = input('user type : ')


def player_trading_history(cursor):
    print('create player trading')
    date = input('date(0000-00-00) : ')
    team_id = input('team ID : ')
    player_id = input('player ID : ')
    player_state = input('player state : ')


create_schema_functions = {
    'player': player,
    'team': team,
    'belongs_to': belongs_to,
    'owner': owner,
    'owns': owns,
    'director': director,
    'directs': directs,
    'awards': awards,
    'player_won': player_won,
    'team_won': team_won,
    'client': client,
}

li = []
def create_data_menu():
    print('**** Register Data ****')
    for i in range(0, len(li)):
        print(f'{i + 1}. {li[i]}')


def create_data_process(cursor: psycopg2.extensions.cursor):
    try:
        index = int(input())
        index -= 1
        create_func = li[index]
        create_schema_functions[create_func](cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def create_data(create_schema_functions: dict, cursor):
    if not create_schema_functions:
        print('No Authorization')
        return

    global li
    li.clear()
    li = list(create_schema_functions)
    create_data_menu()
    create_data_process(cursor)
