class Array:
    def __init__(self, instance=None, length: int = -1):
        self.instance = instance
        self.len_ = length
        self.array = list()
        self.count = 0

    def append(self, obj) -> None:
        if self.len_ != -1 and self.count == self.len_:
            raise Exception("array is full")
        if self.instance and not isinstance(obj, self.instance):
            raise Exception("bad obj passed")
        self.array.append(obj)
        self.count += 1

    def append_all(self, objects):
        for obj in objects:
            self.append(obj)

    def __check(self, index: int, down_lim: int = -1, up_lim: int = -1, affect_len: bool = True):
        if affect_len and self.len_ == -1:
            return True
        if down_lim == -1:
            down_lim = 0
        if up_lim == -1:
            up_lim = self.count
        return down_lim <= index < up_lim

    def __getitem__(self, item: int):
        if self.__check(item, affect_len=False):
            return self.array[item]
        raise Exception("bad index passed")

    def __iter__(self):
        return self.array.__iter__()

    def __setitem__(self, key: int, value):
        if not self.instance or isinstance(value, self.instance):
            if self.__check(key, affect_len=False):
                self.array[key] = value
                mess = None
            else:
                mess = 'Bad Key Passed, entered objects len={}, key={}'.format(self.count, key)
        else:
            mess = 'Bad assignment'
        if mess:
            raise Exception(mess)

    def __str__(self):
        return '[{}]'.format(', '.join([str(i) for i in self.array]))

