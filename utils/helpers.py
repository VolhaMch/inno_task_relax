import random
import string

def random_invalid_search_query(length=12):
    chars = string.punctuation + string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))


def random_typo_string():
    return " ".join(["".join(random.choice("qwertyuiopasdfghjklzxcvbnm")
                             for _ in range(random.randint(3, 10)))
                     for _ in range(random.randint(1, 4))])

def random_garbage():
    return "@#$%^&*()_+=?><~" * 3
