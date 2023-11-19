# update 를 할 수 있는 지 의문...


def update_data_menu(update_schema_functions_list):
    print('**** Update Data ****')
    for i in range(0, len(update_schema_functions_list)):
        print(f'{i + 1}. {update_schema_functions_list[i]}')


def update_data_process(update_schema_functions_list, cursor):
    try:
        index = int(input())
        update_func = update_schema_functions_list[index]
        update_func(cursor)
    except ValueError:
        print('Not a valid integer')
    except IndexError:
        print('Index Out of Bound')


def update_data(update_schema_functions_list, cursor):
    update_data_menu(update_schema_functions_list)
    update_data_process(update_schema_functions_list, cursor)