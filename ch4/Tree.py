from collections import deque

class Tree:
    class Node:
        data = None
        left = None
        right = None

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def bst_from(self, li: list):
        self.root = self.__bst_from(li)

    def __bst_from(self, li: list):
        """
        4.2: Minimal Tree from sorted list
        Builds a complete binary search tree from a list.
        """
        l = sorted(li) # Ensures list is sorted in O(n log n)
        size = len(l)
        if size == 2:
            n = self.Node(l[1])
            n.left = self.Node(l[0])
            return n
        if size == 1:
            return self.Node(l[0])
        n = self.Node(l[int(size/2)])
        n.left = self.__bst_from(l[:int(size/2)])
        n.right = self.__bst_from(l[int(size/2) + 1:])

        return n

    def tree_from(self, li: list):
        self.root = self.__tree_from(li)

    def __tree_from(self, li: list):
        """
        Builds a complete binary tree from a list.
        """
        size = len(l)
        if size == 2:
            n = self.Node(l[1])
            n.left = self.Node(l[0])
            return n
        if size == 1:
            return self.Node(l[0])
        n = self.Node(l[int(size/2)])
        n.left = self.__bst_from(l[:int(size/2)])
        n.right = self.__bst_from(l[int(size/2) + 1:])

        return n

    def depth_first(self):
        l = []
        self.__depth_first(self.root, l)
        return l

    def __depth_first(self, n, l):
        if n:
            self.__depth_first(n.left, l)
            l.append(n.data)
            self.__depth_first(n.right, l)

    def bredth_first(self):
        if self.root == None:
            return []
        n = self.root
        q = deque()
        q.append(n)
        l = []
        while q:
            n = q.popleft()
            l.append(n.data)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return l
