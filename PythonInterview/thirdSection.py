import string
import itertools as it


def execute():
    print("HELLO WORLD".isupper())
    print(string.ascii_uppercase)
    whitespace_set = set(string.whitespace)
    word = "".join(letter for letter in "HELLO WORLD" if letter not in whitespace_set)
    print(word)


def ittertools():
    a = map(pow, range(10), it.repeat(2))
    print(list(a))
    ones = list(it.repeat(1, times=8))
    print(ones)
    friends = ["Jack", "Jill", "Joe"]
    permutations = it.permutations(friends, r=2)
    print(list(permutations))
    combinations = it.combinations(friends, r=2)
    print(list(combinations))


if __name__ == '__main__':
    ittertools()