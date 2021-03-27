def fizz_buzz(numbers):
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"
    return numbers


def list_comprehension(numbers):
    square = [x ** 2 for x in numbers]
    print(square)
    odd = [x for x in numbers if x % 2 == 1]
    print(odd)
    rows = 2
    columns = 3
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    print(matrix)
    # Find a number with max square
    print(max(numbers, key=lambda x: x * x))


# Learning about f-string
class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"""
        My name is {self.name},
        I am {self.age} years old
        """


# Learning about sort
def sorting():
    animals = ["cat", "dog", "cheetah", "rhino"]
    print(sorted(animals, reverse=True))
    animals = [
        {"type": "cat", "name": "Stephanie", "age": 8},
        {"type": "dog", "name": "Devon", "age": 3},
        {"type": "rhino", "name": "Moe", "age": 5}
    ]
    # This dont change the list
    print(sorted(animals, key=lambda animal: animal["age"]))
    print(animals)
    # This change the list
    animals.sort(key=lambda animal: animal["age"])
    print(animals)


if __name__ == '__main__':
    sorting()
