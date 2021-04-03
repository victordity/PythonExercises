import itertools as it


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):

    cart = list(it.product(priceOfJeans, priceOfShoes))
    cart1 = [sum(possibility) for possibility in cart if sum(possibility) <= dollars]
    cart2 = list(it.product(cart1, priceOfSkirts))
    cart3 = [sum(possibility) for possibility in cart2 if sum(possibility) <= dollars]
    cart4 = list(it.product(cart3, priceOfTops))
    cart5 = [sum(possibility) for possibility in cart4 if sum(possibility) <= dollars]
    print(len(cart5))


def storage(n, m, h, v):
    storage = [[0] * (n + 1) for row in range(m + 1)]
    print(storage)
    new_row = [1 for _ in range(n + 1)]
    for separator in h:
        storage[separator - 1] = new_row
        storage[separator] = new_row
    # Remove the vertical separators
    for separator in v:
        for row in storage:
            row[separator - 1] = 1
            row[separator] = 1
    print(storage)


if __name__=='__main__':
    storage(3, 3, [2], [2])