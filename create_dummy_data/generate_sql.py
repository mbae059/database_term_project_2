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


def merge_sql_files(input_folder, output_file):
    with open(output_file, 'w') as merged_file:
        # drop tables first
        for table in tables:
            merged_file.write(f'drop table if exists {table};\n')

        # insert query
        for filename in os.listdir(input_folder):
            if filename.endswith('.sql'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r') as sql_file:
                    merged_file.write(sql_file.read() + '\n')

if __name__ == "__main__":
    input_folder_path = './sql'
    output_file_path = '../input_query.sql'

    merge_sql_files(input_folder_path, output_file_path)

    print("SQL files merged successfully.")
