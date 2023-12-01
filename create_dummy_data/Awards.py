file = open('sql/awards.sql', 'w')

for i in range(1, 101):
    file.write(f"insert into awards (awards_name) values ('team_award_#{i}');\n")

for i in range(1, 101):
    file.write(f"insert into awards (awards_name) values ('individual_award_#{i}');\n")
