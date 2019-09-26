from typing import List


class Matrix:
    def __init__(self, *args: int):
        self.vol = args
        self.matrix = []

        def make(matrix: list, index: int = 0):
            for i in range(args[index]):
                if index == len(args) - 1:
                    matrix.append(None)
                else:
                    matrix.append([])
                    make(matrix[i], index + 1)
        make(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __iter__(self):
        return self.matrix

    def __setitem__(self, key, value):
        self.matrix.__setitem__(key, value)

    def __str__(self):
        return str(self.matrix)
