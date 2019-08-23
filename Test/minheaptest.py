from ds import MinHeap


if __name__ == '__main__':
    h = MinHeap()
    h.add(10)
    h.add(100)
    h.add(7)
    h.add(12)
    h.add(11)
    h.add(5)
    h.add(1)
    h.add(9)
    h.add(4)
    print(h)
    print('7', h.search(7))
    print('60', h.search(60))
    h.remove(1)
    print('1', h)
    h.remove(7)
    print('7', h)
    h.remove(100)
    print('100', h)
