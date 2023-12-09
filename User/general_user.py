from user_interface import UserInterface
from CRUD import read, delete, update, create


class GeneralUser(UserInterface):
    register_schema_functions = {
    }
    read_schema_functions = {
        'player': read.player,
        'team': read.team,
        'belongs_to': read.belongs_to,
        'owner': read.owner,
        'owns': read.owns,
        'director': read.director,
        'directs': read.directs,
        'awards': read.awards,
        'player_won': read.player_won,
        'team_won': read.team_won,
    }

    update_schema_functions = {
    }

    delete_schema_functions = {
    }

    register_schema_functions_list = list(register_schema_functions)
    read_schema_functions_list = list(read_schema_functions)
    update_schema_functions_list = list(update_schema_functions)
    delete_schema_functions_list = list(delete_schema_functions)
    def get_menu(self):
        print('Menu:')
        print('1. Read')
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

