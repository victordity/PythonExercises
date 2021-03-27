import sys
from collections import defaultdict, Counter, deque, namedtuple


def sets(s):
    """
    Sets are a unordered collection of unique values
    Its a dict made only by keys, and the keys can not be equals
    """
    seen_c = set(s)
    seen_d = {k for k in s}
    return seen_d


def generators():
    """
    Generators are a special type of iterator that you can use to iterate over a sequence of values
     Generators are a useful way to iterate through a sequence using constant memory. Here’s an example:
    """
    g = (i for i in range(6))
    lst = [i for i in range(1, 1001)]
    g = (i for i in range(1, 1001))
    print(sys.getsizeof(lst))  # 4516
    print(sys.getsizeof(g))  # 64
    # Doing this you can save a lot of memory
    return g


student_grades = defaultdict(list, {"Alice": [10, 20]})


def dictionaries(name, score):
    """
    collections.defaultdict is a subclass of the dictionary data structure that allows for default values if
    the key does not exist in the dictionary:
    """
    student_grades[name].append(score)
    print(student_grades)


def counter(s):
    """
    This class is very useful to count the frequency of elements in an iterable
    """
    print(Counter(s))


def deck():
    """
    Deques allow for appending to both left and right and popping from both left and right in constant time.
    """
    deq = deque([1, 2, 3])
    deq.appendleft(5)
    deq.append(6)
    print(deq)
    deq.popleft()
    print(deq)


def named_tuples():
    """
    namedtuple is a subclass of tuples and creates tuple-like immutable objects
    Can be used to build like classes that the attributes will not change
    """
    Car = namedtuple("Car", ["color", "make", "model", "mileage"])
    my_car = Car(color="midnight silver", make="Tesla", model="Model Y", mileage=5)
    print(my_car.color)


if __name__ == '__main__':
    print(sets("aabb"))
    generators()
    dictionaries("Joe", 10)
    counter("aabbccd")
    deck()
    named_tuples()
