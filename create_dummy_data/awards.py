file = open('sql/awards.sql', 'w')

for i in range(1, 101):
    file.write(f"insert into awards (name) values ('award#{i}');\n")

