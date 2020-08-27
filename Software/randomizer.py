import string
import random

def digit_random_string(longitud):
    result_str = ''.join(random.choice(string.digits) for i in range(longitud))
    return result_str
