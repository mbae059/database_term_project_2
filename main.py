import psycopg2
import user

if __name__ == '__main__':
    user = user.User()

    try:
        con = psycopg2.connect(
            database='db_trade',
            user='sudo',
            password='qwe123',
            host='::1',
            port='5432',
        )
        con.autocommit = True

        cursor = con.cursor()

        while not user.login(cursor):
            print("Wrong ID and Password!")

        while True:
            user.get_menu()  # display menu
            user.query(cursor)

    except psycopg2.OperationalError as e:
        print('Error: Unable to connect to the database.')
        print('Error message: ')
        print(e)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if con:
            con.close()
            print('Connection closed.')