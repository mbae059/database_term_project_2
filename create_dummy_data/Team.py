import random

file = open('sql/team.sql', 'w')

for i in range(1,11):
    file.write(f"insert into team (name, establishment_year) values ('team#{i}', {random.randint(1950, 1970)});\n")
