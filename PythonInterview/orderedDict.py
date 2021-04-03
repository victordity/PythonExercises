from collections import defaultdict, OrderedDict


student_grades = defaultdict(list)


def defaultdict():
    student_grades["Jhon"]
    print(student_grades)


def fromKey():
    color_level = {"red": 2, "blue": 5, "black": 8, "white": 9}
    colors = list(dict.fromkeys(color_level))
    print(colors)


def orderedDict():
    numbers = OrderedDict(one=1, two=2, three=3, four=4)
    print(numbers)

    letters = OrderedDict(b=3, d=1, a=4, c=2)
    print(sorted(letters, key=lambda value: letters[value]))
    for key in sorted(letters):
        letters.move_to_end(key)

    print(letters)


if __name__ == '__main__':
    orderedDict()
