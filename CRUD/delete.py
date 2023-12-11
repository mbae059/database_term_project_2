import psycopg2


def player(cursor):
    print('delete player records...')
    id = input('player id : ')

    query = f"delete from player where id = {id}"

    try:
        cursor.execute(query)
        print("player records deleted!")
    except Exception as e:
        print(e)


def team(cursor):
    print('delete team records...')
    id = input('team id : ')

    query = f"delete from team where id = {id}"

    try:
        cursor.execute(query)
        print("team records deleted!")
    except Exception as e:
        print(e)


def belongs_to(cursor):
    print('delete belongs_to records...')

    id = input('belongs_to id : ')

    query = f"delete from belongs_to where id = {id}"

    try:
        cursor.execute(query)
        print("belongs_to records deleted!")
    except Exception as e:
        print(e)


def owner(cursor):
    print('delete owner records...')

    id = input('owner id : ')

    query = f"delete from owner where id = {id}"

    try:
        cursor.execute(query)
        print("owner records deleted!")
    except Exception as e:
        print(e)


def owns(cursor):
    print('delete owns records...')

    id = input('owns id : ')

    query = f"delete from owns where id = {id}"

    try:
        cursor.execute(query)
        print("owns records deleted!")
    except Exception as e:
        print(e)


def director(cursor):
    print('delete director records...')

    id = input('director id : ')

    query = f"delete from director where id = {id}"

    try:
        cursor.execute(query)
        print("director records deleted!")
    except Exception as e:
        print(e)


def directs(cursor):
    print('delete directs records...')

    id = input('directs id : ')

    query = f"delete from directs where id = {id}"

    try:
        cursor.execute(query)
        print("directs records deleted!")
    except Exception as e:
        print(e)


def awards(cursor):  # budget 이 예산? 그렇다면 signing bonus...
    print('delete awards records...')

    id = input('awards id : ')

    query = f"delete from awards where id = {id}"

    try:
        cursor.execute(query)
        print("awards records deleted!")
    except Exception as e:
        print(e)


def player_won(cursor):
    print('delete player_won records...')

    id = input('player_won id : ')

    query = f"delete from player_won where id = {id}"

    try:
        cursor.execute(query)
        print("player_won records deleted!")
    except Exception as e:
        print(e)


def team_won(cursor):
    print('delete team_won records...')

    id = input('team_won id : ')

    query = f"delete from team_won where id = {id}"

    try:
        cursor.execute(query)
        print("team_won records deleted!")
    except Exception as e:
        print(e)


def client(cursor):
    print('delete client records...')

    id = input('client id : ')

    query = f"delete from client where id = {id}"

    try:
        cursor.execute(query)
        print("client records deleted!")
    except Exception as e:
        print(e)


delete_schema_functions = {
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
def delete_data_menu():
    print('**** Delete Data ****')
    for i in range(0, len(li)):
        print(f'{i + 1}. {li[i]}')


def delete_data_process(cursor: psycopg2.extensions.cursor):
    try:
        index = int(input())
        index -= 1
        delete_func = li[index]
        delete_schema_functions[delete_func](cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def delete_data(delete_schema_functions: dict, cursor):
    if not delete_schema_functions:
        print('No Authorization')
        return

    global li
    li.clear()
    li = list(delete_schema_functions)
    delete_data_menu()
    delete_data_process(cursor)
