file = open('sql/awards.sql', 'w')

cnt = 1
for i in range(1, 101):
    file.write(f"insert into awards values ('{cnt}', 'team_award_#{i}')\n")
    cnt += 1

for i in range(1, 101):
    file.write(f"insert into awards values ('{cnt}', 'individual_award_#{i}')\n")
    cnt += 1