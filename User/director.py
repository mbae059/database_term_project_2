from user_interface import UserInterface
from CRUD import create, read, update, delete


class Director(UserInterface):
    create_schema_functions = {
        'belongs_to': (create.belongs_to, read.belongs_to),
        'directs': (create.directs, read.directs),
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
        'client': read.client,
    }

    update_schema_functions = {
        'belongs_to': (update.belongs_to, read.belongs_to),
        'directs': (update.directs, read.directs),
    }

    delete_schema_functions = {
    }

    create_schema_functions_list = list(create_schema_functions)
    read_schema_functions_list = list(read_schema_functions)
    update_schema_functions_list = list(update_schema_functions)
    delete_schema_functions_list = list(delete_schema_functions)

    def get_menu(self):
        print('Menu:')
        print('1. Register')
        print('2. Read')
        print('3. Update')
        print('Press any other key to exit')
        return

    def query(self, cursor):
        choice = int(input())
        if choice == 1:
            create.create_data(self.create_schema_functions, cursor)
        elif choice == 2:
            read.read_data(self.read_schema_functions, cursor)
        elif choice == 3:
            update.update_data(self.update_schema_functions, cursor)
        else:
            return

