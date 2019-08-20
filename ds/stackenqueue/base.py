class Base:
    def __init__(self):
        self.__list = list()
        self.__len = 0

    def push(self, obj):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    @property
    def length(self):
        return self.__len
