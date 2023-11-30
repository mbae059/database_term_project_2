import random

def generate_korean_phone_number():
    # Korean phone numbers generally have the format 01X-XXXX-XXXX
    # where X is any digit
    number_format = "010-{1:04d}-{2:04d}".format(
        random.randint(0, 9),
        random.randint(0, 9999),
        random.randint(0, 9999)
    )
    return number_format

# Example usage:

def get_phone_number():
    random_phone_number = generate_korean_phone_number()
    return random_phone_number
