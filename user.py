import getpass

import psycopg2

from user_interface import UserInterface
from User.admin import Admin
from User.agent import Agent
from User.director import Director
from User.general_user import GeneralUser
from User.owner import Owner
from User.player import Player


# return user_name, team_id, user_type
# just a parser
def get_user_information(user_information):
    # user_information is a tuple consisting of client_id, client_name, client_password, team_id, client_type
    client_id, client_name, client_password, team_id, client_type = user_information
    return client_name, team_id, client_type


class User:
    def __init__(self, user_interface: UserInterface = None):
        self.user_id = ""
        self.user_name = ""
        self.team_id = ""
        self.user_type = ""
        self.user_interface = user_interface  # using Dependency Injection

    def login(self, cursor):
        id = input("ID: ")
        # password = getpass.getpass("password: ")
        password = input("password: ")

        # TODO get user information using id and password
        cursor.execute(f'select * from client where client_name = \'{id}\' and client_password = \'{password}\'')

        result = cursor.fetchone()

        if result is None:
            return False

        user_name, team_id, user_type = get_user_information(result)
        self.user_id = id
        self.user_name = user_name
        self.team_id = team_id
        self.user_type = user_type

        print(f'You logged in as a {user_type}')

        if user_type == 'admin':
            self.set_user_type(Admin())
        elif user_type == 'player':
            self.set_user_type(Player())
        elif user_type == 'director':
            self.set_user_type(Director())
        elif user_type == 'owner':
            self.set_user_type(Owner())
        elif user_type == 'agent':
            self.set_user_type(Agent())
        elif user_type == 'general_user':
            self.set_user_type(GeneralUser())
        else:
            print('Fatal Error. Database User schema user_type is contaminated')
            return False

        return True

    # used for dependency injection
    # setter for user_interface
    def set_user_type(self, user_interface: UserInterface):
        self.user_interface = user_interface

    def debug(self):
        print(f"debug type : {self.user_type}")

    def get_menu(self):
        self.user_interface.get_menu()

    def query(self, cursor):
        self.user_interface.query(cursor)