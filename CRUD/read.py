import psycopg2


def player(cursor):
    print('read user records...')

    query = f"select * from player"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def team(cursor):
    print('read team records...')

    query = f"select * from team"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def belongs_to(cursor):
    print('read belongs_to records...')

    query = f"select * from belongs_to"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def owner(cursor):
    print('read owner records...')

    query = f"select * from owner"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def owns(cursor):
    print('read owns records...')

    query = f"select * from owns"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def director(cursor):
    print('read director records...')

    query = f"select * from director"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def directs(cursor):
    print('read directs records...')

    query = f"select * from directs"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def awards(cursor):  # budget 이 예산? 그렇다면 signing bonus...
    print('read awards records...')

    query = f"select * from awards"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def player_won(cursor):
    print('read player_won records...')

    query = f"select * from player_won"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def team_won(cursor):
    print('read team_won records...')

    query = f"select * from team_won"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


def client(cursor):
    print('read client records...')

    query = f"select * from client"

    try:
        cursor.execute(query)

        rows = cursor.fetchall()

        print([desc[0] for desc in cursor.description])

        # Print each row
        for row in rows:
            print(row)
    except Exception as e:
        print(e)


read_schema_functions = {
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


def read_data_menu():
    print('**** read Data ****')
    for i in range(0, len(li)):
        print(f'{i + 1}. {li[i]}')


def read_data_process(cursor: psycopg2.extensions.cursor):
    try:
        index = int(input())
        index -= 1
        read_func = li[index]
        read_schema_functions[read_func](cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')




def read_data(read_schema_functions: dict, cursor):
    if not read_schema_functions:
        print('No Authorization')
        return

    global li
    li.clear()
    li = list(read_schema_functions)
    read_data_menu()
    read_data_process(cursor)
