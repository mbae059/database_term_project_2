from CRUD import read, delete, update, create
from user_interface import UserInterface


class Director(UserInterface):
    register_schema_functions = {
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
        'player': (update.player, read.player),
        'team': (update.team, read.team),
        'belongs_to': (update.belongs_to, read.belongs_to),
        'owner': (update.owner, read.owner),
        'owns': (update.owns, read.owns),
        'director': (update.director, read.director),
        'directs': (update.directs, read.directs),
        'awards': (update.awards, read.awards),
        'player_won': (update.player_won, read.player_won),
        'team_won': (update.team_won, read.team_won),
        'client': (update.client, read.client),
    }

    delete_schema_functions = {
        'player': (delete.player, read.player),
        'team': (delete.team, read.team),
        'belongs_to': (delete.belongs_to, read.belongs_to),
        'owner': (delete.owner, read.owner),
        'owns': (delete.owns, read.owns),
        'director': (delete.director, read.director),
        'directs': (delete.directs, read.directs),
        'awards': (delete.awards, read.awards),
        'player_won': (delete.player_won, read.player_won),
        'team_won': (delete.team_won, read.team_won),
        'client': (delete.client, read.client),
    }

    register_schema_functions_list = list(register_schema_functions)
    read_schema_functions_list = list(read_schema_functions)
    update_schema_functions_list = list(update_schema_functions)
    delete_schema_functions_list = list(delete_schema_functions)

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

