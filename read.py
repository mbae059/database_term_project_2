def player(cursor):
    print('read user')


def player_record(cursor):
    print('read player_record')


def agent(cursor):
    print('read agent')


def owner(cursor):
    print('read owner')


def team(cursor):
    print('read team')


def director(cursor):
    print('read director')


def user(cursor):
    print('read user')


def player_agent(cursor):  # budget 이 예산? 그렇다면 signing bonus...
    print('read player_agent')


def player_trading(cursor):
    print('read player trading')


def team_awards(cursor):
    print('read team awards')


def individual_awards(cursor):
    print('read individual awards')


def awards_name(cursor):
    print('read awards name')


def baseball_records(cursor):
    print('read baseball records')


def baseball_stadium(cursor):
    print('read baseball stadium')


def read_data_menu(read_schema_functions_list):
    print('**** Read Data ****')
    for i in range(0, len(read_schema_functions_list)):
        print(f'{i + 1}. {read_schema_functions_list[i]}')


def read_data_process(read_schema_functions_list, cursor):
    try:
        index = int(input())
        read_func = read_schema_functions_list[index]
        read_func(cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def read_data(read_schema_functions_list, cursor):
    read_data_menu()
    read_data_process(cursor)
