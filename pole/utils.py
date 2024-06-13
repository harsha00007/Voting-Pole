import random
import string


def vote_id_number():
    random_characters = ""
    for _ in range(3):
        random_character_choice = random.choice(string.ascii_uppercase)
        random_characters += random_character_choice
    random_number = random.randrange(1000000, 9999999)
    vote_id = random_characters + str(random_number)
    return vote_id
