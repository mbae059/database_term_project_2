import os

tables = [
    'Player',
    'Agent',
    'Owner',
    'Team',
    'Director',
    'Client',
    'Player_Agent',
    'Team_Award',
    'Individual_Award',
    'Awards',
    'Baseball_Records',
    'Baseball_Stadium'
]

def drop_table(output_file):
    with open(output_file, 'w') as merged_file:
        for table in tables:
            merged_file.write(f'drop table if exists {table};\n')

def create_table(output_file):
    input_file = './DDL_query.sql'
    with open(output_file, 'a') as merged_file:
        with open(input_file, 'r') as ddl_query_sql:
            merged_file.write(ddl_query_sql.read() + '\n')

def create_insert_query(input_folder, output_file):
    with open(output_file, 'a') as merged_file:
        # insert query
        for filename in os.listdir(input_folder):
            if filename.endswith('.sql'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r') as sql_file:
                    merged_file.write(sql_file.read() + '\n')

def set_foreign_key(output_file):
    input_file = '../foreign_key.sql'
    with open(output_file, 'a') as merged_file:
        with open(input_file, 'r') as foreign_key_sql:
            merged_file.write(foreign_key_sql.read() + '\n')


def merge_sql_files(input_folder, output_file):
    drop_table(output_file)
    create_table(output_file)
    create_insert_query(input_folder, output_file)
    set_foreign_key(output_file)

if __name__ == "__main__":
    input_folder_path = './sql'
    output_file_path = '../input_query.sql'

    merge_sql_files(input_folder_path, output_file_path)

    print("SQL files merged successfully.")
