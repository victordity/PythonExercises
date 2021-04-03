from collections import Counter, defaultdict
from math import floor
import string


def easy(s):
    n = len(s)
    a = Counter(s)
    b = [x[0] for x in a.items() if x[1] > (n // 2)]
    print([idx for idx, x in enumerate(s) if x in b])


def keypad_string(keys):
    """
    Given a string consisting of 0-9, find the string that is created usint
    a stardart phone keypad
    """
    # Build keyboard
    possible_letters = string.ascii_lowercase
    possible_keys = string.digits
    keyboard = defaultdict(list)
    start_index = 0
    for key in possible_keys:
        if key == "0":
            keyboard[key] = " "
        elif key == "1":
            keyboard[key] = ""
        else:
            num_letters = 4 if key in {"7", "9"} else 3
            keyboard[key] = possible_letters[start_index:start_index + num_letters]
            start_index += num_letters
    # Build word typed
    current_key = ""
    count = 0
    word = []
    for idx, key in enumerate(keys):
        if key == "1":
            pass
        if current_key == "":
            current_key = key
            count = 1
        elif key == current_key:
            count += 1
        if idx == len(keys) - 1 or key != keys[idx + 1]:
            # Append letters to the word
            num_letters = 4 if key in {"7", "9"} else 3
            while count > num_letters:
                word.append(keyboard[key][-1])
                count -= num_letters
            word.append(keyboard[key][count - 1])
            count = 1
            current_key = key


    print(keyboard)


if __name__ == '__main__':
    keypad_string("77777777778")
