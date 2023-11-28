file = open('./awards.sql', 'w')

for i in range(1, 101):
    file.write(f"insert into awards values ('award_#{i}')\n")