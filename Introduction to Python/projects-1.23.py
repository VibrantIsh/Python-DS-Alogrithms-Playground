#P-1.23 Write a python program that output all the possible strings formed by using the characters 'c', 'a', 't', 'd', 'o', and 'g' exactly once.


import random

characters = 'catdog'
generated_strings = set()

while True:
    string_length = random.randint(1, 10)  # Random string length, maximum 10 characters
    random_string = ''.join(random.choice(characters) for i in range(string_length))

    if random_string not in generated_strings:
        generated_strings.add(random_string)
        print(random_string)
        break


