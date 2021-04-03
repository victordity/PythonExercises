import bisect


def bisect_tutorial():
    fruits = ["apple", "banana", "banana", "banana", "orange", "pineapple"]
    print(bisect.bisect(fruits, "banana"))
    print(bisect.bisect_left(fruits, "banana"))
    occurrences = bisect.bisect(fruits, "banana") - bisect.bisect_left(fruits, "banana")
    print(occurrences) # Number of occurrences of the word banana

    bisect.insort_left(fruits, "kiwi")
    print(fruits)


def binary_iterative(elements, search_item):
    """Return the index of the search_item element."""

    left, right = 0, len(elements) - 1

    while left <= right:

        middle_idx = (left + right) // 2
        middle_element = elements[middle_idx]

        if middle_element == search_item:
            return middle_idx
        if middle_element < search_item:
            left = middle_idx + 1
        elif middle_element > search_item:
            right = middle_idx - 1

    return None


if __name__ == '__main__':
    elements = [3, 4, 5, 5, 9]
    a = binary_iterative(elements, 5)
    print(a)
