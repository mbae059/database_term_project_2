import os
import subprocess

tables = [
    'player',
    'team',
    'belongs_to',
    'owner',
    'owns',
    'director',
    'directs',
    'awards',
    'player_won',
    'team_won',
    'client',
]


def drop_table(output_file):
    with open(output_file, 'w') as merged_file:
        for table in tables:
            merged_file.write(f'drop table if exists {table};\n')


def create_table(output_file):
    input_file = 'create_table.sql'
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

def merge_sql_files(input_folder, output_file):
    drop_table(output_file)
    create_table(output_file)
    create_insert_query(input_folder, output_file)


files_to_execute = [
    "player.py",
    "team.py",
    "belongs_to.py",
    "owner.py",
    "owns.py",
    "director.py",
    "directs.py",
    "awards.py",
    "player_won.py",
    "team_won.py",
    "client.py",
]
if __name__ == "__main__":
    for file in files_to_execute:
        subprocess.run(["python", file])

    input_folder_path = './sql'
    output_file_path = '../input_query.sql'

    merge_sql_files(input_folder_path, output_file_path)

    print("SQL files merged successfully.")
