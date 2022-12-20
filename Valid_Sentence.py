import re
import string


# This function first checks if the string starts with a capital letter. If not,
# it returns False. Next, it checks if the string has an even number of quotation marks.
# If not, it returns False. It then checks if the string ends with a sentence termination character,
# and if it has any period characters other than the last character. If either of these checks fail,
# the function returns False. Finally, the function checks if any numbers below 13 are spelled out in the string.
# If any of these numbers are found, the function returns False. If the string passes all of these checks,
# the function returns True.

def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # Use the translate() method to remove the punctuation
    no_punctuation = input_string.translate(translator)

    return no_punctuation

def is_valid_sentence(sentence):
    # Check if the string starts with a capital letter
    if not sentence[0].isupper():
        return False

    # Check if the string has an even number of quotation marks
    if sentence.count('"') % 2 != 0:
        return False

    # Check if the string ends with a sentence termination character
    if not sentence[-1] in [".", "?", "!"]:
        return False

    # Check if the string has any period characters other than the last character
    if re.search(r'\.(?!$)', sentence):
        return False
    # Check if numbers below 13 are spelled out,

    for word in sentence.split():
        if word.isnumeric():
            for i in range(1, 13):
                if i == int(word):

                    return False

    # If all checks pass, the string is a valid sentence
    return True


print(is_valid_sentence("The quick brown fox said \"hello Mr lazy dog\"."))
print(is_valid_sentence("The quick brown fox said hello Mr lazy dog."))
print(is_valid_sentence("One lazy dog is too few, 13 is too many."))
print(is_valid_sentence("One lazy dog is too few, thirteen is too many."))
print(is_valid_sentence("How many \"lazy dogs\" are there?"))

print(is_valid_sentence("The quick brown fox said \"hello Mr. lazy dog\"."))
print(is_valid_sentence("the quick brown fox said \"hello Mr lazy dog\"."))
print(is_valid_sentence("The quick brown fox said \"hello Mr lazy dog."))
print(is_valid_sentence("One lazy dog is too few, 12 is too many."))
# 11, and 12, don't get parsed properly as an integer by int()
# so need to remove any punctuation
print(is_valid_sentence(remove_punctuation("Are there 11, 12, or 13 lazy dogs?")))
print(is_valid_sentence("There is no punctuation in this sentence"))