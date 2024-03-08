import random
import string

# creating random shortcode for the URL
def generate_random_shortcode():
    max_length = 6
    characters = string.ascii_letters + "_" + string.digits
    shortcode = ''.join(random.sample(characters, max_length))
    return shortcode


def in_use_shortcode(shortcode):
    shortcode_in_use = ["9pqIug", "voyExA", "dSFugI", "nb0C9h", "P7c_Ez", "asd123"]
    return shortcode in shortcode_in_use


# https://www.w3schools.com/python/ref_string_isalnum.asp
def is_valid_shortcode(shortcode):
    valid_characters = shortcode.isalnum() or "_"
    return len(shortcode)==6 and valid_characters and not in_use_shortcode(shortcode)

#checking the functions behaviour
shortcode = generate_random_shortcode()
print(shortcode)
print(in_use_shortcode(shortcode))
print(is_valid_shortcode(shortcode))