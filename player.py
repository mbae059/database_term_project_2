import getpass

import read
import update
import user
import create

class Player(user):
    register_schema_list = \
        [
            'player','player_record', 'player_agent', 'player_trading' # only player schema should be modified...?
        ]
    read_schema_list = \
        [
            'player', 'player_record', 'agent', 'owner', 'team', 'director', 'player_agent',
            'player_trading', 'team_awards', 'individual_awards', 'awards_name', 'baseball_records',
            'baseball_stadium'
        ] # user schema has been excluded

    def __init__(self):
        super(self)

    def get_menu(self, cursor):
        print('Menu:')
        print('1. Register')
        print('2. Read')
        print('3. Update')
        print('4. Delete')
        print('Any Other Key To Exit')

        choice = int(input())
        if choice==1:
            Player.register_data(cursor)
        elif choice==2:
            Player.read_data(cursor)
        elif choice==3:
            Player.update_data()
        elif choice==4:
            Player.delete_data()
        else:
            return


    def register_data(self, cursor):
        print('**** Register Data ****')
        for i in range(0, len(Player.access_schema)):
            print(f'{i + 1}. {Player.access_schema[i]}')

        database_schema = input()

        if database_schema not in super_user.access_schema:
            super().error()
            return

        if database_schema is 'player':
            create.player(cursor)
            read.player(cursor)
        elif database_schema is 'player_record':
            create.player_record(cursor)
            read.player_record(cursor)
        elif database_schema is 'agent':
            create.agent(cursor)
            read.agent(cursor)
        elif database_schema is 'owner':
            create.owner(cursor)
            read.owner(cursor)
        elif database_schema is 'team':
            create.team(cursor)
            read.team(cursor)
        elif database_schema is 'director':
            create.director(cursor)
            read.director(cursor)
        elif database_schema is 'user':
            create.user(cursor)
            read.user(cursor)
        elif database_schema is 'player_agent':
            create.player_agent(cursor)
            read.player_agent(cursor)
        elif database_schema is 'player_trading':
            create.player_trading(cursor)
            read.player_trading(cursor)
        elif database_schema is 'team_awards':
            create.team_awards(cursor)
            read.team_awards(cursor)
        elif database_schema is 'individual_awards':
            create.individual_awards(cursor)
            read.individual_awards(cursor)
        elif database_schema is 'awards_name':
            create.awards_name(cursor)
            read.awards_name(cursor)
        elif database_schema is 'baseball_records':
            create.baseball_records(cursor)
            read.baseball_records(cursor)
        elif database_schema is 'baseball_stadium':
            create.baseball_stadium(cursor)
            read.baseball_stadium(cursor)
        else:
            super().error()

    def read_data(self, cursor):
        print('**** Read Data ****')
        for i in range(0, len(super_user.access_schema)):
            print(f'{i + 1}. {super_user.access_schema[i]}')

        database_schema = input()

        if database_schema not in super_user.access_schema:
            super().error()
            return

        if database_schema is 'player':
            read.player(cursor)
        elif database_schema is 'player_record':
            read.player_record(cursor)
        elif database_schema is 'agent':
            read.agent(cursor)
        elif database_schema is 'owner':
            read.owner(cursor)
        elif database_schema is 'team':
            read.team(cursor)
        elif database_schema is 'director':
            read.director(cursor)
        elif database_schema is 'user':
            read.user(cursor)
        elif database_schema is 'player_agent':
            read.player_agent(cursor)
        elif database_schema is 'player_trading':
            read.player_trading(cursor)
        elif database_schema is 'team_awards':
            read.team_awards(cursor)
        elif database_schema is 'individual_awards':
            read.individual_awards(cursor)
        elif database_schema is 'awards_name':
            read.awards_name(cursor)
        elif database_schema is 'baseball_records':
            read.baseball_records(cursor)
        elif database_schema is 'baseball_stadium':
            read.baseball_stadium(cursor)
        else:
            super().error()

    def update_data(self, cursor):
        print('**** Update Data ****')
        for i in range(0, len(super_user.access_schema)):
            print(f'{i + 1}. {super_user.access_schema[i]}')

        database_schema = input()

        if database_schema not in super_user.access_schema:
            super().error()
            return

        if database_schema is 'player':
            update.player(cursor)
        elif database_schema is 'player_record':
            update.player_record(cursor)
        elif database_schema is 'agent':
            update.agent(cursor)
        elif database_schema is 'owner':
            update.owner(cursor)
        elif database_schema is 'team':
            update.team(cursor)
        elif database_schema is 'director':
            update.director(cursor)
        elif database_schema is 'user':
            update.user(cursor)
        elif database_schema is 'player_agent':
            update.player_agent(cursor)
        elif database_schema is 'player_trading':
            update.player_trading(cursor)
        elif database_schema is 'team_awards':
            update.team_awards(cursor)
        elif database_schema is 'individual_awards':
            update.individual_awards(cursor)
        elif database_schema is 'awards_name':
            update.awards_name(cursor)
        elif database_schema is 'baseball_records':
            update.baseball_records(cursor)
        elif database_schema is 'baseball_stadium':
            update.baseball_stadium(cursor)
        else:
            super().error()