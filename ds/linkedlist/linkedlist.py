from typing import TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __str__(self):
        return '{}'.format(self.data.__str__())


class LinkedList:
    def __init__(self):
        self._head = Node(0)
        self._last = self._head

    def add(self, obj):
        self._last.next = Node(obj)
        self._last = self._last.next
        self._head.data += 1

    def remove(self, key: T) -> T:
        node = self._head
        while node.next:
            if node.next.data.__eq__(key):
                tmp = node.next
                node.next = node.next.next
                if not node.next:
                    self._last = node
                self._head.data -= 1
                return tmp
            node = node.next
        return None

    def remove_index(self, key: int):
        if not isinstance(key, int):
            raise Exception("Key must be a integer")
        if key >= self.size or key < 0:
            raise Exception("Bad key passed")
        i: int = 0
        node = self._head
        while i < key:
            node = node.next
            i += 1
        tmp = node.next
        node.next = node.next.next
        if not node.next:
            self._last = node
        self._head.data -= 1
        return tmp

    def get(self, key):
        node = self._head
        while node.next:
            if node.next.data.__eq__(key):
                return node.next.data
            node = node.next
        return None

    def get_index(self, key: int):
        if not isinstance(key, int):
            raise Exception("Key must be integer")
        if key < 0 or key >= self.size:
            raise Exception("Bad key passed")
        i = 0
        node = self._head
        while i < key:
            i += 1
            node = node.next
        return node.next

    def __iter__(self):
        node = self._head
        while node.next:
            yield node.next.data
            node = node.next

    @property
    def size(self):
        return self._head.data
