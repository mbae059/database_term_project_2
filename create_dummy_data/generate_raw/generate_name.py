import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # includes both lowercase and uppercase letters and digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_strings_under_10(length_limit=10, num_strings=10):
    for _ in range(num_strings):
        string_length = random.randint(5, length_limit - 1)  # generate lengths from 1 to length_limit - 1
        random_string = generate_random_string(string_length)
        yield random_string

# Example usage:

def get_name():
    string_generator = generate_strings_under_10()
    random_string = next(string_generator)
    return random_string
if __name__ == "__main__" :
    string_generator = generate_strings_under_10()

    for _ in range(10):
        random_string = next(string_generator)
        print(random_string)
