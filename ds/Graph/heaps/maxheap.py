from ds import GBase


class MaxHeap(GBase):
    def __init__(self):
        self.__list = list()
        self.__len = 0

    @staticmethod
    def __replace(_list_: list, i: int, j: int):
        tmp = _list_[i]
        _list_[i] = _list_[j]
        _list_[j] = tmp

    def add(self, obj):
        self.__len += 1
        self.__list.append(obj)
        index = self.__len - 1
        while index >= 1 and obj > self.__list[index // 2]:
            self.__replace(self.__list, index, index // 2)
            index //= 2

    def search(self, key):
        for obj in self.__list:
            if obj == key:
                return obj
        return None

    def remove(self, key):
        for i in range(self.__len):
            if self.__list[i] == key:
                self.__len -= 1
                deleted = self.__list.pop(i)
                tmp = self.__list.pop()
                self.__list.insert(i, tmp)
                self.__heapify(i)
                del tmp
                return deleted

    def __heapify(self, index: int):
        left_child, right_child = index * 2 + 1, index * 2 + 2
        if index != 0 and self.__list[index] > self.__list[index // 2]:
            self.__replace(self.__list, index, index // 2)
            self.__heapify(index // 2)
        elif left_child < self.__len and right_child < self.__len:
            if self.__list[index] < self.__list[left_child] or \
                    self.__list[index] < self.__list[right_child]:
                max_index = left_child if self.__list[left_child] >= self.__list[right_child] else right_child
                self.__replace(self.__list, index, max_index)
                self.__heapify(max_index)
        elif left_child < self.__len and self.__list[left_child] > self.__list[index]:
            self.__replace(self.__list, index, left_child)
            self.__heapify(left_child)

    def __str__(self):
        return '[{}]'.format(', '.join([str(i) for i in self.__list]))

    def __iter__(self):
        for i in range(self.__len):
            yield self.__list[i]

    @property
    def length(self):
        return self.__len
