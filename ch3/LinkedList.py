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
        if len(args) == 0:
            self.head = None
            self.len = 0
            return
        if type(args[0]) == list and len(args) == 1:
            args = args[0]
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

    def __kth_from_last(self, k):

        if k < 1:
            return None

        curr_node = self.head
        length = 0
        while curr_node:
            length += 1
            curr_node = curr_node.next
        if k > length:
            return None
        curr_node = self.head
        curr_index = 0
        while curr_node:
            if curr_index == length - k:
                return curr_node
            curr_node = curr_node.next
            curr_index += 1

        return None

    def node_at(self, index):
        if index < 0:
            return self.__kth_from_last(abs(index))

        curr_node = self.head
        curr_index = 0

        while curr_node:
            if curr_index == index:
                return curr_node

            curr_node = curr_node.next
            curr_index += 1

        return None

    def append_to_tail(self, v):
        if self.len == 0:
            self.append_to_front(v)
            return
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

    def append_node_to_tail(self, n):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = n
        self.len += 1

