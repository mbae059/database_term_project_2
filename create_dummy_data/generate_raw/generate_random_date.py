from datetime import datetime, timedelta
import random

def generate_random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%Y-%m-%d')

# Example usage:

if __name__ == "__main__":
    start_date = datetime(1990, 1, 1)
    end_date = datetime(2003, 12, 31)
    print(generate_random_date(start_date, end_date))