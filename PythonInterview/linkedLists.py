from collections import deque


def deque_methods():
    a = deque(['a', 'b', 'c'])
    b = deque("abc")
    c = deque([{'data': 'a'}, {'data': 'b'}])
    b.append('e')
    print(b)
    b.pop()
    print(b)
    b.appendleft(0)
    print(b)
    b.popleft()
    print(b)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


def execute():
    # Build a linked list in python
    llist = LinkedList
    first_node = Node("a")
    llist.head = first_node
    second_node = Node("b")
    third_node = Node("c")
    first_node.next = second_node
    second_node.next = third_node
    print(repr(llist))


if __name__ == '__main__':
    execute()
