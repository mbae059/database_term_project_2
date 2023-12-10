from user_interface import UserInterface
from CRUD import create, read, update, delete


class Admin(UserInterface):
    create_schema_functions = {
        'player': (create.player, read.player),
        'team': (create.team, read.team),
        'belongs_to': (create.belongs_to, read.belongs_to),
        'owner': (create.owner, read.owner),
        'owns': (create.owns, read.owns),
        'director': (create.director, read.director),
        'directs': (create.directs, read.directs),
        'awards': (create.awards, read.awards),
        'player_won': (create.player_won, read.player_won),
        'team_won': (create.team_won, read.team_won),
        'client': (create.client, read.client),
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
            create.create_data(self.create_schema_functions, cursor)
        elif choice == 2:
            read.read_data(self.read_schema_functions, cursor)
        elif choice == 3:
            update.update_data(self.update_schema_functions, cursor)
        elif choice == 4:
            delete.delete_data(self.delete_schema_functions, cursor)
        else:
            return

