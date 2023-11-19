import read
import update
from user_interface import UserInterface
import create
import read
import update
import delete


class Owner(UserInterface):
    register_schema_functions = {
        'player': (create.player, read.player),
        'player_record': (create.player_record, read.player_record),
        'team': (create.team, read.team),
        'director': (create.director, read.director),
    }
    read_schema_functions = {
        'player': read.player,
        'player_record': read.player_record,
        'agent': read.agent,
        'owner': read.owner,
        'team': read.team,
        'director': read.director,
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
        'owner': (update.owner, read.owner),
        'team': (update.team, read.team),
        'director': (update.director, read.director),
    }
    delete_schema_functions = {
        'player': (delete.player, read.player),
        'player_record': (delete.player_record, read.player_record),
        'agent': (delete.agent, read.agent),
        'team': (delete.team, read.team),
        'director': (delete.director, read.director),
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

