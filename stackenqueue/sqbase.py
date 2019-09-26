class SQBase:
    def __init__(self):
        self._list = list()
        self._len = 0
        self._name = 'Base'

    def push(self, obj):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    @property
    def length(self):
        return self._len

    def isempty(self):
        return self._len == 0
