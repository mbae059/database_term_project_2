import psycopg2


def player(cursor):
    print('create user records...')
    name = input('player name : ')
    position = input('position : ')
    birth = input('birth(0000-00-00): ')

    query = f"INSERT INTO player (name, position, birth) VALUES ('{name}', '{position}', '{birth}')"

    try:
        cursor.execute(query)
        print("player records created!")
    except Exception as e:
        print(e)


def team(cursor):
    print('create team records...')
    name = input('team name : ')
    establishment_year = input('establishment year(1900~2023) : ')

    query = f"INSERT INTO team (name, establishment_year) VALUES ('{name}', {establishment_year})"

    try:
        cursor.execute(query)
        print("team records created!")
    except Exception as e:
        print(e)


def belongs_to(cursor):
    print('create belongs_to records...')
    print('This is a table about player that belongs to a certain team')
    print('DO NOT TRY TO CREATE TUPLE UNLESS YOU HAVE INFORMATION ABOUT PLAYER ID AND TEAM ID AS THIS TABLE REQUIRES THIS')

    player_id = input('player id : ')
    team_id = input('team id : ')
    start_date = input('start date(0000-00-00) : ')
    uniform_number = input('uniform number : ')
    contract_term = input('contract term : ')
    contract_payment = input('contract payment : ')

    query = (f"INSERT INTO belongs_to (player_id, team_id, start_date, uniform_number, contract_term, contract_payment) "
             f"VALUES ({player_id}, {team_id}, '{start_date}', {uniform_number}, {contract_term}, {contract_payment})")

    try:
        cursor.execute(query)
        print("belongs_to records created!")
    except Exception as e:
        print(e)


def owner(cursor):
    print('create owner records...')
    name = input('name : ')
    age = input('age : ')
    budget = input('budget : ')

    query = f"INSERT INTO owner (name, age, budget) VALUES ({name}, {age}, {budget})"

    try:
        cursor.execute(query)
        print("owner records created!")
    except Exception as e:
        print(e)


def owns(cursor):
    print('create owns records...')
    print('DO NOT TRY TO CREATE TUPLE UNLESS YOU HAVE INFORMATION ABOUT OWNER ID THIS TABLE REQUIRES THIS')

    owner_id = input('owner id : ')
    team_id = input('team id : ')

    query = f"INSERT INTO owns (owner_id, team_id) VALUES ({owner_id}, {team_id})"

    try:
        cursor.execute(query)
        print("owns records created!")
    except Exception as e:
        print(e)


def director(cursor):
    print('create director records...')
    name = input('director name : ')
    start_date = input('director start date(0000-00-00) : ')

    query = f"INSERT INTO director (name, start_date) VALUES ({name}, '{start_date}')"

    try:
        cursor.execute(query)
        print("director records created!")
    except Exception as e:
        print(e)


def directs(cursor):
    print('create directs records...')
    print('DO NOT TRY TO CREATE TUPLE UNLESS YOU HAVE INFORMATION ABOUT DIRECTOR ID AND TEAM ID AS THIS TABLE REQUIRES THIS')

    director_id = input('director id : ')
    team_id = input('team id : ')
    contract_term = input('contract term : ')
    start_date = input('start date(0000-00-00) : ')
    contract_payment = input('contract payment : ')

    query = (f"INSERT INTO directs (director_id, team_id, contract_term, start_date, contract_payment) "
             f"VALUES ({director_id}, {team_id}, {contract_term}, '{start_date}', {contract_payment})")

    try:
        cursor.execute(query)
        print("directs records created!")
    except Exception as e:
        print(e)

def awards(cursor):
    print('create awards records...')
    name = input('awards name : ')

    query = f"INSERT INTO awards (name) VALUES ('{name}')"

    try:
        cursor.execute(query)
        print("directs records created!")
    except Exception as e:
        print(e)


def player_won(cursor):
    print('create player_won records...')
    print('DO NOT TRY TO CREATE TUPLE UNLESS YOU HAVE INFORMATION ABOUT PLAYER ID AND AWARD ID AS THIS TABLE REQUIRES THIS')
    player_id = input('player id : ')
    awards_id = input('awards id : ')

    query = f"INSERT INTO player_won (player_id, awards_id) VALUES ({player_id},{awards_id})"

    try:
        cursor.execute(query)
        print("player_won records created!")
    except Exception as e:
        print(e)


def team_won(cursor):
    print('create team_won records...')
    print('DO NOT TRY TO CREATE TUPLE UNLESS YOU HAVE INFORMATION ABOUT TEAM ID AND AWARD ID AS THIS TABLE REQUIRES THIS')
    team_id = input('player id : ')
    awards_id = input('awards id : ')

    query = f"INSERT INTO team_won (team_id, awards_id) VALUES ({team_id},{awards_id})"

    try:
        cursor.execute(query)
        print("team_won records created!")
    except Exception as e:
        print(e)


def client(cursor):
    print('create client records...')

    name = input('client ID : ')
    password = input('client password : ')
    team_id = input('team id : ')
    client_type = input('client type(admin, player, director, owner, general_user) : ')

    query = f"INSERT INTO client (name, password, team_id, client_type) VALUES ('{name}', '{password}', {team_id}, '{client_type}')"

    try:
        cursor.execute(query)
        print("client records created!")
    except Exception as e:
        print(e)

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
