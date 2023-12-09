import psycopg2
import user

if __name__ == '__main__':
    user = user.User()

    con = psycopg2.connect(
        database='db_trade',
        user='sudo',
        password='qwe123',
        host='::1',
        port='5432',
    )

    cursor = con.cursor()

    while not user.login(cursor):
        print("Wrong ID and Password!")

    while True:
        user.get_menu()  # display menu
        user.query(cursor)
