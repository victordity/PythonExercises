import itertools as it

def fizzBuzz(n):
    result = []
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(number)
    return result


def encode(cards):
    suits = ["c", "d", "h", "s"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    deck = list(it.product(suits, value))
    encoded_cards = [deck.index((card[1], card[0])) for card in cards]

    return sorted(encoded_cards)


def decode(cards):
    suits = ["c", "d", "h", "s"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
    deck = list(it.product(suits, value))
    cards = sorted(cards)
    decoded_cards = [f"{deck[card][1]}{deck[card][0]}" for card in cards]
    return decoded_cards


if __name__ == '__main__':
    print(encode(['Ac', 'Ks', '5h', 'Td', '3c']))
    print(decode([0, 51, 30, 22, 2]))
