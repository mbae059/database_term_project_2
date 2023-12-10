from datetime import datetime
import random
from create_dummy_data.generate_raw.generate_random_date import generate_random_date

file = open('sql/player.sql', 'w')

j = 1
cnt = 0
start_date = datetime(1980, 1, 1)
end_date = datetime(1990, 12, 31)

# 10 team
# 10 players in one team
for i in range(1, 11):
    j = (i-1) * 10 + 1

    positions = [
        'P',
        'C',
        '1B',
        '2B',
        '3B',
        'SS',
        'LF',
        'CF',
        'RF',
        'DH',
    ]
    for k in range(10):
        file.write(f"insert into player (name, position, birth) values ('player#{j+k}', '{positions[k]}', '{generate_random_date(start_date, end_date)}');\n")

# positions of baseball
# P, C, 1B, 2B, 3B, SS, LF, CF, RF, DH
