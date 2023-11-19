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

    # update query


def player_record(cursor):
    print('create player_record')
    player_id = input('player id : ')
    start_date = input('start date : ')
    end_date = input('end date(NULLABLE) : ')
    team_id = input('team id : ')


def agent(cursor):
    print('create agent')
    agent_name = input('agent name : ')
    age = input('age : ')
    player_id = input('player id : ')  # shouldn't this be deleted?
    contact_info = input('contact info : ')


def owner(cursor):
    print('create owner')
    team_id = input('team id : ')
    owner_name = input('owner name : ')
    owner_age = input('owner age : ')
    budget = input('budget : ')


def team(cursor):
    print('create team')
    team_name = input('team name : ')
    owner_ID = input('owner id : ')
    director_ID = input('director id : ')
    establishment_year = input('establishment year : ')


def director(cursor):
    print('create director')
    director_name = input('director name : ')
    director_year = input('director year : ')
    team_id = input('team id : ')
    income = input('income : ')


"""
There should be various user types
User(user_ID, user_name, team_id, type)

type kind:

admin, player, agent, owner, director 
"""
def user(cursor):
    print('create user')
    user_ID = input('user ID : ')
    user_name = input('user name : ')
    team_id = input('team id : ')
    type = input('user type : ')


def player_agent(cursor):  # budget 이 예산? 그렇다면 signing bonus...
    print('create player_agent')
    agent_id = input('agent ID : ')
    player_id = input('player ID : ')
    team_id = input('team ID : ')
    contract_date = input('contract date : ')
    contract_term = input('contract term : ')
    signing_bonus = input('signing bonus : ')


def player_trading(cursor):
    print('create player trading')
    date = input('date(0000-00-00) : ')
    team_id = input('team ID : ')
    player_id = input('player ID : ')
    player_state = input('player state : ')


def team_awards(cursor):
    print('create team awards')
    awards_id = input('awards id : ')
    year = input('year : ')
    team_id = input('team id : ')


def individual_awards(cursor):
    print('create individual awards')
    awards_id = input('awards id : ')
    year = input('year : ')
    player_id = input('player id : ')


def awards_name(cursor):
    print('create awards name')
    awards_name = input('awards name : ')


def baseball_records(cursor):
    print('create baseball records')
    team1_id = input('team1 id : ')
    team2_id = input('team2 id : ')
    baseball_stadium_id = input('baseball stadium id : ')
    score = input('score(0, 0) : ')


def baseball_stadium(cursor):
    print('create baseball stadium')
    location = input('location : ')
    area = input('area : ')
    capacity = input('capacity : ')


def update_data_menu(update_schema_functions_list):
    print('**** Update Data ****')
    for i in range(0, len(update_schema_functions_list)):
        print(f'{i + 1}. {update_schema_functions_list[i]}')


def update_data_process(update_schema_functions_list, cursor):
    try:
        index = int(input())
        update_func = update_schema_functions_list[index]
        update_func(cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def update_data(update_schema_functions_list, cursor):
    if not update_schema_functions_list:
        print('No Authorization')
        return
    update_data_menu(update_schema_functions_list)
    update_data_process(update_schema_functions_list, cursor)