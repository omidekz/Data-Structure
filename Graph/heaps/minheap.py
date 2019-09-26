from ds import GBase


class MinHeap(GBase):
    def __init__(self):
        self.__list = list()
        self.__len = 0

    @staticmethod
    def __replace(__list__: list, i: int, j: int):
        tmp = __list__[i]
        __list__[i] = __list__[j]
        __list__[j] = tmp

    def add(self, obj):
        """
        add obj to heap and use of __gt__ method
        :param obj:
        :return:
        """
        self.__list.append(obj)
        index = self.__len
        self.__len += 1
        while index >= 1 and self.__list[index].__lt__(self.__list[index // 2]):
            self.__replace(self.__list, index, index // 2)
            index = index // 2

    def search(self, key):
        for obj in self.__list:
            if obj.__eq__(key):
                return obj
        return None

    def remove(self, key):
        for i in range(len(self.__list)):
            if self.__list[i].__eq__(key):
                deleted = self.__list.pop(i)
                self.__len -= 1
                tmp = self.__list.pop()
                self.__list.insert(i, tmp)
                self.__heapify(i)
                return deleted
        return None

    def __heapify(self, i: int):
        lc, rc = 2 * i + 1, 2*i+2
        if i != 0 and self.__list[i] < self.__list[i // 2]:
            self.__replace(self.__list, i, i // 2)
            self.__heapify(i // 2)
        elif lc < self.__len and rc < self.__len:
            if self.__list[i] > self.__list[lc] or self.__list[i] > self.__list[rc]:
                min_index = lc if self.__list[lc] <= self.__list[rc] else rc
                self.__replace(self.__list, i, min_index)
                self.__heapify(min_index)
        elif lc < self.__len and \
                self.__list[i] > self.__list[lc]:
            self.__replace(self.__list, i, lc)
            self.__heapify(lc)

    def __str__(self):
        return '[{}]'.format(', '.join([str(i) for i in self.__list]))

    def __iter__(self):
        for i in range(self.__len):
            yield self.__list[i]

    @property
    def length(self):
        return self.__len
