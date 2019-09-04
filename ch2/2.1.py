import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

# These are the best two options.
# We could sort, then delete. But the fastest sort would be O(nlogn) time, with O(n) space.
# Heap sort would work it was not a linked list, but since it is a linked list, we loose
# our ability to access a random part of the array in constant time.

def remove_dupes_1(ll: LinkedList) -> LinkedList:
    """
    Removes duplicate values in a LinkedList
    Time complexity: O(n^2), where n = len(ll)
    Space Complexity: O(1)
    >>> remove_dupes_1(LinkedList(1))
    [1]
    >>> remove_dupes_1(LinkedList(1, 1))
    [1]
    >>> remove_dupes_1(LinkedList(1, 2, 3, 4))
    [1, 2, 3, 4]
    >>> remove_dupes_1(LinkedList(1, 1, 1, 2, 2, 8, 5, 5, 5, 2, 2, 3, 4))
    [1, 2, 8, 5, 3, 4]
    >>> remove_dupes_1(LinkedList(1, 2, 3, 4, 4, 4, 4, 4))
    [1, 2, 3, 4]
    """

    slow = ll.head

    while(slow):
        fast = slow

        while(fast.next):
            if slow.val == fast.next.val:
                fast.next = fast.next.next
            else:
                fast = fast.next

        slow = slow.next

    return ll

def remove_dupes_2(ll: LinkedList) -> LinkedList:
    """
    Removes duplicate values in a LinkedList
    Time complexity: O(n)
    Space Complexity: O(n)
    >>> remove_dupes_2(LinkedList(1))
    [1]
    >>> remove_dupes_2(LinkedList(1, 1))
    [1]
    >>> remove_dupes_2(LinkedList(1, 2, 3, 4))
    [1, 2, 3, 4]
    >>> remove_dupes_2(LinkedList(1, 1, 1, 2, 2, 8, 5, 5, 5, 2, 2, 3, 4))
    [1, 2, 8, 5, 3, 4]
    >>> remove_dupes_2(LinkedList(1, 2, 3, 4, 4, 4, 4, 4))
    [1, 2, 3, 4]
    """

    if not ll.head.next:
        return ll

    curr = ll.head
    my_set = {curr.val}

    while curr.next:
        if curr.next.val in my_set:
            curr.next = curr.next.next
        else:
            my_set.add(curr.next.val)
            curr = curr.next
    return ll

doctest.testmod()

