import getpass
class User:
    def __init__(self):
        self.id = ""

    def login(self, cursor):
        id = input("ID: ")
        password = getpass.getpass("password: ")

        cursor.execute(f'select password from user where user_id={id}')

        result = cursor.fetchall()

        # TODO result[0][0] should be fixed when the database schema is determined
        if password is result[0][0]:
            print('You logged in as a {blank}')
            name = cursor.execute(f'get id from database')
            self.id = name
            return True
        else:
            return False
        # if id and password matches then pass
        # if it doesn't then return false

    def get_menu(self):
        print("implement get_menu!")

    def query(self, cursor):
        print("implement query")

    def error(self):
        print("Error! The input is incorrect!")

