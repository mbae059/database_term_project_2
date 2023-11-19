def delete_data_menu(delete_schema_functions_list):
    print('**** Delete Data ****')
    for i in range(0, len(delete_schema_functions_list)):
        print(f'{i + 1}. {delete_schema_functions_list[i]}')


def delete_data_process(delete_schema_functions_list, cursor):
    try:
        index = int(input())
        delete_func = delete_schema_functions_list[index]
        delete_func(cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def delete_data(delete_schema_functions_list, cursor):
    delete_data_menu(delete_schema_functions_list)
    delete_data_process(delete_schema_functions_list, cursor)
