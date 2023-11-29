import getpass

import psycopg2

from user_interface import UserInterface
from User.admin import Admin

# TODO implement
def get_user_information(user_information):
    pass


class User:
    def __init__(self, user_interface: UserInterface = None):
        self.user_id = ""
        self.user_name = ""
        self.team_id = ""
        self.user_type = ""
        self.user_interface = user_interface # using Dependency Injection

    def login(self, cursor: psycopg2.cursor):
        id = input("ID: ")
        password = getpass.getpass("password: ")

        # TODO get user information using id and password
        cursor.execute(f'TODO get user information using id and password')

        result = cursor.fetchone()

        if result is None:
            return False

        user_name, team_id, user_type = get_user_information(result)
        self.user_id = id
        self.user_name = user_name
        self.team_id = team_id
        self.user_type = user_type

        print(f'You logged in as a {user_type}')

        if user_type is 'admin':
            self.set_user_type(Admin())
        elif user_type is 'player':
            self.set_user_type(Player())
        elif user_type is 'director':
            self.set_user_type(Director())
        elif user_type is 'owner':
            self.set_user_type(Owner())
        elif user_type is 'agent':
            self.set_user_type(Agent())
        elif user_type is 'general_user':
            self.set_user_type(GeneralUser())
        else:
            print('Fatal Error. Database User schema user_type is contaminated')
            return False

        return True

    def set_user_type(self, user_interface: UserInterface):
        self.user_interface = user_interface

    def get_menu(self):
        self.user_interface.get_menu()

    def query(self, cursor: psycopg2.cursor):
        self.user_interface.query(cursor)
