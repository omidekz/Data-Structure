from ds import Base


class Stack(Base):
    def __init__(self):
        super().__init__()

    def push(self, obj):
        self.__list.append(obj)
        self.__len += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is Empty")
        self.__len -= 1
        return self.__list.pop()

    def peek(self):
        obj = self.pop()
        self.push(obj)
        return obj
