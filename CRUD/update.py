import psycopg2


def player(cursor):
    print('update player records...')
    print('id will be used as key to locate the tuple')
    id = input('player id : ')

    name = input('player name : ')
    position = input('position : ')
    birth = input('birth(0000-00-00): ')

    query = f"update player set name = '{name}', position = '{position}', birth ='{birth}' where id = {id}"

    try:
        cursor.execute(query)
        print("player records updated!")
    except Exception as e:
        print(e)


def team(cursor):
    print('update team records...')
    print('id will be used as key to locate the tuple')
    id = input('team id : ')

    name = input('team name : ')
    establishment_year = input('establishment year : ')

    query = f"update team set name = '{name}', establishment_year = '{establishment_year}' where id = {id}"

    try:
        cursor.execute(query)
        print("team records updated!")
    except Exception as e:
        print(e)


def belongs_to(cursor):
    print('update belongs_to records...')
    print('id will be used as key to locate the tuple')
    print('This table is for keeping the records of player transfer, thus this table should not be updated')

    id = input('belongs_to id : ')

    player_id = input('player id : ')
    team_id = input('team id : ')
    start_date = input('start date : ')
    uniform_number = input('uniform_number : ')
    contract_term = input('contract term : ')
    contract_payment = input('contract payment : ')

    query = (f"update belongs_to set player_id = {player_id}, team_id = {team_id}, start_date ='{start_date}', "
             f"uniform_number={uniform_number}, contract_term={contract_term}, contract_payment={contract_payment} where id = {id}")

    try:
        cursor.execute(query)
        print("belongs_to records updated!")
    except Exception as e:
        print(e)


def owner(cursor):
    print('update owner records...')
    print('id will be used as key to locate the tuple')
    id = input('owner id : ')

    name = input('owner name : ')
    age = input('owner age : ')
    budget = input('budget: ')

    query = f"update owner set name = '{name}', age = '{age}', budget ='{budget}' where id = {id}"

    try:
        cursor.execute(query)
        print("owner records updated!")
    except Exception as e:
        print(e)


def owns(cursor):
    print('update user records...')
    print('id will be used as key to locate the tuple')
    id = input('owns id : ')

    owner_id = input('owner id : ')
    team_id = input('team id : ')

    query = f"update owns set owner_id = {owner_id}, team_id = {team_id} where id = {id}"

    try:
        cursor.execute(query)
        print("owns records updated!")
    except Exception as e:
        print(e)


def director(cursor):
    print('update director records...')
    print('id will be used as key to locate the tuple')
    id = input('director id : ')

    name = input('director name : ')
    start_date = input('the start of the career(0000-00-00): ')

    query = f"update director set name = '{name}', start_date = '{start_date}' where id = {id}"

    try:
        cursor.execute(query)
        print("director records updated!")
    except Exception as e:
        print(e)


def directs(cursor):
    print('update directs records...')
    print('id will be used as key to locate the tuple')
    id = input('directs id : ')

    director_id = input('director id : ')
    team_id = input('team id : ')
    contract_term = input('contract term: ')
    start_date = input('directing start date(0000-00-00): ')
    contract_payment = input('contract payment: ')
    query = (f"update directs set director_id = {director_id}, team_id = {team_id}, contract_term = {contract_term}, "
             f"start_date = '{start_date}', contract_payment = {contract_payment} where id = {id}")

    try:
        cursor.execute(query)
        print("directs records updated!")
    except Exception as e:
        print(e)

def awards(cursor):
    print('update awards records...')
    print('id will be used as key to locate the tuple')
    id = input('awards id : ')

    name = input('awards name : ')

    query = f"update awards set name = '{name}' where id = {id}"

    try:
        cursor.execute(query)
        print("awards records updated!")
    except Exception as e:
        print(e)


def player_won(cursor):
    print('update player_won records...')
    print('id will be used as key to locate the tuple')
    id = input('player_won id : ')

    player_id = input('player id : ')
    awards_id = input('awards id : ')

    query = f"update player_won set player_id = {player_id}, awards_id = {awards_id} where id = {id}"

    try:
        cursor.execute(query)
        print("player_won records updated!")
    except Exception as e:
        print(e)


def team_won(cursor):
    print('update team_won records...')
    print('id will be used as key to locate the tuple')
    id = input('team_won id : ')

    team_id = input('team id : ')
    awards_id = input('awards id : ')

    query = f"update team_won set team_id = {team_id}, awards_id = {awards_id} where id = {id}"

    try:
        cursor.execute(query)
        print("team_won records updated!")
    except Exception as e:
        print(e)


def client(cursor):
    print('update client records...')
    print('id will be used as key to locate the tuple')
    id = input('client id : ')

    name = input('client name : ')
    password = input('client password : ')
    team_id = input('supporting team_id : ')
    client_type = input('client type : ')

    query = f"update client set name = '{name}', password = '{password}', team_id ={team_id}, client_type='{client_type}' where id = {id}"

    try:
        cursor.execute(query)
        print("client records updated!")
    except Exception as e:
        print(e)

update_schema_functions = {
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
def update_data_menu():
    print('**** Update Data ****')
    for i in range(0, len(li)):
        print(f'{i + 1}. {li[i]}')


def update_data_process(cursor: psycopg2.extensions.cursor):
    try:
        index = int(input())
        index -= 1
        update_func = li[index]
        update_schema_functions[update_func](cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def update_data(updates_schema_functions: dict, cursor):
    if not updates_schema_functions:
        print('No Authorization')
        return

    global li
    li.clear()
    li = list(updates_schema_functions)
    update_data_menu()
    update_data_process(cursor)
