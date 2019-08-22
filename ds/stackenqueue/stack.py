from ds import SQBase


class Stack(SQBase):
    def __init__(self):
        super().__init__()
        self.__name = 'Stack'

    def push(self, obj):
        self._list.append(obj)
        self._len += 1

    def pop(self):
        if self.isempty():
            raise Exception("{} is Empty".format(self.__name))
        self._len -= 1
        return self._list.pop()

    def peek(self):
        obj = self.pop()
        self.push(obj)
        return obj
