from user_interface import UserInterface
from CRUD import read, delete, update, create


class General_User(UserInterface):
    register_schema_functions = {
        'player': (create.player, read.player),
        'player_record': (create.player_record, read.player_record),
        'agent': (create.agent, read.agent),
        'owner': (create.owner, read.owner),
        'team': (create.team, read.team),
        'director': (create.director, read.director),
        'user': (create.user, read.user),
        'player_agent': (create.player_agent, read.player_agent),
        'player_trading': (create.player_trading, read.player_trading),
        'team_awards': (create.team_awards, read.team_awards),
        'individual_awards': (create.individual_awards, read.individual_awards),
        'awards_name': (create.awards_name, read.awards_name),
        'baseball_records': (create.baseball_records, read.baseball_records),
        'baseball_stadium': (create.baseball_stadium, read.baseball_stadium)
    }
    read_schema_functions = {
        'player': read.player,
        'player_record': read.player_record,
        'agent': read.agent,
        'owner': read.owner,
        'team': read.team,
        'director': read.director,
        'user': read.user,
        'player_agent': read.player_agent,
        'player_trading': read.player_trading,
        'team_awards': read.team_awards,
        'individual_awards': read.individual_awards,
        'awards_name': read.awards_name,
        'baseball_records': read.baseball_records,
        'baseball_stadium': read.baseball_stadium,
    }
    update_schema_functions = {
        'player': (update.player, read.player),
        'player_record': (update.player_record, read.player_record),
        'agent': (update.agent, read.agent),
        'owner': (update.owner, read.owner),
        'team': (update.team, read.team),
        'director': (update.director, read.director),
        'user': (update.user, read.user),
        'player_agent': (update.player_agent, read.player_agent),
        'player_trading': (update.player_trading, read.player_trading),
        'team_awards': (update.team_awards, read.team_awards),
        'individual_awards': (update.individual_awards, read.individual_awards),
        'awards_name': (update.awards_name, read.awards_name),
        'baseball_records': (update.baseball_records, read.baseball_records),
        'baseball_stadium': (update.baseball_stadium, read.baseball_stadium)
    }
    delete_schema_functions = {
        'player': (delete.player, read.player),
        'player_record': (delete.player_record, read.player_record),
        'agent': (delete.agent, read.agent),
        'owner': (delete.owner, read.owner),
        'team': (delete.team, read.team),
        'director': (delete.director, read.director),
        'user': (delete.user, read.user),
        'player_agent': (delete.player_agent, read.player_agent),
        'player_trading': (delete.player_trading, read.player_trading),
        'team_awards': (delete.team_awards, read.team_awards),
        'individual_awards': (delete.individual_awards, read.individual_awards),
        'awards_name': (delete.awards_name, read.awards_name),
        'baseball_records': (delete.baseball_records, read.baseball_records),
        'baseball_stadium': (delete.baseball_stadium, read.baseball_stadium)
    }
    register_schema_functions_list = list(register_schema_functions)
    read_schema_functions_list = list(read_schema_functions)
    update_schema_functions_list = list(update_schema_functions)
    delete_schema_functions_list = list(delete_schema_functions)

    def __init__(self):
        super(self)

    def get_menu(self):
        print('Menu:')
        print('1. Register')
        print('2. Read')
        print('3. Update')
        print('4. Delete')
        print('Press any other key to exit')
        return

    def query(self, cursor):
        choice = int(input())
        if choice == 1:
            create.register_data(self.register_schema_functions_list, cursor)
        elif choice == 2:
            read.read_data(self.read_schema_functions_list, cursor)
        elif choice == 3:
            update.update_data(self.update_schema_functions_list, cursor)
        elif choice == 4:
            delete.delete_data(self.delete_schema_functions_list, cursor)
        else:
            return

