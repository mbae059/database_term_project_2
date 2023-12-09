def player(cursor):
    print('create user')
    player_name = input('player name : ')
    team_name = input('team name : ')
    team_id = input('team id : ')
    position = input('position : ')
    uniform_number = input('uniform number : ')
    birth = input('birth : ')
    income = input('income : ')
    agent_id = input('agent_id : ')

    # create query


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
    if not read_schema_functions_list:
        print('No Authorization')
        return
    read_data_menu(read_schema_functions_list)
    read_data_process(read_schema_functions_list, cursor)
