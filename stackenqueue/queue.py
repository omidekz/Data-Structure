from ds import Stack


class Queue(Stack):
    def __init__(self):
        super().__init__()
        self.__name = 'Queue'

    def push(self, obj):
        self._list.insert(0, obj)
        self._len += 1

    def peek(self):
        if self.isempty():
            raise Exception("{} is empty".format(self.__name))
        obj = self._list.pop()
        self._list.append(obj)
        return obj
