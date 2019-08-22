class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        return '{}'.format(self.data.__str__())


class BST:
    def __init__(self):
        self.root = None

    def add(self, obj):
        """
        This method add obj to bst
        :param obj:
        :return:
        """
        if not self.root:
            self.root = Node(obj)
        else:
            self.__add(self.root, obj)

    @staticmethod
    def __add(node: Node, obj):
        """
        This method add the obj depend on __gt__ method
        :param node:
        :param obj:
        :return:
        """
        if node.data < obj:
            if node.right:
                BST.__add(node.right, obj)
            else:
                node.right = Node(obj)
        else:
            if node.left:
                BST.__add(node.left, obj)
            else:
                node.left = Node(obj)

    def search(self, key):
        return self.__search(self.root, key).data

    @staticmethod
    def __search(node: Node, key):
        if not node:
            return None
        if key == node.data:
            return node
        if key > node.data:
            return BST.__search(node.right, key)
        return BST.__search(node.left, key)

    def remove(self, key):
        if self.root.data == key:
            tmp = self.root
            if tmp.right is None and tmp.left is None:
                self.root = None
            elif tmp.right and tmp.left:
                tmp = tmp.right
                while tmp.left:
                    tmp = tmp.left
                tmp = self.__remove(self.root, tmp.data)
                left = self.root.left
                right = self.root.right
                tmp.left = left
                tmp.right = right
                self.root = tmp
            else:
                if tmp.right:
                    self.root = tmp.right
                else:
                    self.root = tmp.left
            return tmp.data
        else:
            return self.__remove(self.root, key).data

    @staticmethod
    def __remove(node: Node, key) -> Node:
        if node:
            if node.right and node.right.data.__eq__(key):
                tmp = node.right
                if tmp.right is None and tmp.left is None:
                    node.right = None
                elif tmp.right and tmp.left:
                    tmp = tmp.right
                    while tmp.left:
                        tmp = tmp.left
                    tmp = BST.__remove(node, tmp.data)
                    left = node.right.left
                    right = node.right.right
                    tmp.left = left
                    tmp.right = right
                    node.right = tmp
                else:
                    if tmp.right:
                        node.right = node.right.right
                    else:
                        node.right = node.right.left
                return tmp
            elif node.left and node.left.data.__eq__(key):
                tmp = node.left
                if tmp.right is None and tmp.left is None:
                    node.left = None
                elif tmp.right and tmp.left:
                    tmp = tmp.right
                    while tmp.left:
                        tmp = tmp.left
                    tmp = BST.__remove(node, tmp.data)
                    left = node.left.left
                    right = node.left.right
                    tmp.left = left
                    tmp.right = right
                    node.left = tmp
                else:
                    if tmp.right:
                        node.left = node.left.right
                    else:
                        node.left = node.left.left
                return tmp
            elif key > node.data:
                return BST.__remove(node.right, key)
            else:
                return BST.__remove(node.left, key)

    def __iter__(self):
        """
        DFS PreOrder
        :return:
        """
        from ds import Stack
        stack = Stack()
        stack.push(self.root)
        while not stack.isempty():
            tmp = stack.pop()
            if not tmp:
                break
            if tmp.right:
                stack.push(tmp.right)
            if tmp.left:
                stack.push(tmp.left)
            yield tmp.data
