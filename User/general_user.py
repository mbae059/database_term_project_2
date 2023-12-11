from user_interface import UserInterface
from CRUD import create, read, update, delete


class GeneralUser(UserInterface):
    create_schema_functions = {
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
    }

    delete_schema_functions = {
    }


    def get_menu(self):
        print('Menu:')
        print('1. Read')
        print('Press any other key to exit')
        return

    def query(self, cursor):
        choice = int(input())
        if choice == 1:
            read.read_data(self.read_schema_functions, cursor)
        else:
            return

