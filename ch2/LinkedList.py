# Python3
# LinkList module
# Created By Harrison Hayes
class SinglyLinkedList:
    """
    Implementation of the Singly Linked List Data Structure.
    """
    class Node:
        def __init__(self, v):
            self.val = v
            self.next  = None

    def __init__(self, *args):
        self.head = self.Node(args[-1])
        self.len = 1
        for arg in reversed(args[:-1]):
            self.append_to_front(arg)

    def __repr__(self):
        l = []
        curr = self.head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return str(l)

    def __str__(self):
        return self.__repr__()

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        pass

    def append_to_tail(self, v):
        temp = self.Node(v)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = temp
        self.len += 1

    def append_to_front(self, v):
        temp = self.Node(v)
        temp.next = self.head
        self.head = temp
        self.len += 1

