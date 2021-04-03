import itertools as it
from random import shuffle


def combinations():
    """Return successive n-length combinations of elements in the iterable."""
    print(list(it.combinations([1, 2, 3], 2)))
    # (1, 2), (1, 3), (2, 3)
    print(list(it.combinations([1, 2, 3])))


def combinations_with_replacement():
    """Return successive n-length combinations of elements in the iterable allowing
    individual elements to have successive repeats."""
    print(list(it.combinations_with_replacement([1, 2, 3], 3)))
    # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
    print(list(it.combinations_with_replacement([1, 2, 3], 2)))
    # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


def permutations():
    """Return successive n-length permutations of elements in the iterable."""
    print(list(it.permutations("abc")))
    # [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
    print(list(it.permutations([1, 2, 3])))
    # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


def repeat():
    """Create an iterator which returns the object for the specified number of times.
    repeat(object, times=1)"""
    print(list(it.repeat("Dity", 5)))


def accumulate():
    """Return series of accumulated sums (or other binary function results).
    accumulate(iterable, func=operator.add)"""
    print(list(it.accumulate([1, 2, 3])))
    # [1, 3, 6]
    print(list(it.accumulate(list(range(1, 11)))))


def product():
    """Cartesian product of input iterables. Equivalent to nested for-loops.
    product(*iterables, repeat=1)"""
    print(list(it.product([1, 2], ['a', 'b'])))
    # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
    deck = list(it.product([2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"],
                           ["Ouro", "Copas", "Paus", "Espada"]))
    shuffle(deck)
    print(deck)


def tee():
    """Create any number of independent iterators from a single input iterable."""
    iter1, iter2 = it.tee(['a', 'b', 'c'], 2)

    print(list(iter1))
    print(list(iter2))


def chain():
    """Chain two lists"""
    print(list(it.chain([1, 2, 3], "abc", "def")))
    # [1, 2, 3, 'a', 'b', 'c', 'd', 'e', 'f']


if __name__ == '__main__':
    chain()
