import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

def loop_beginning(ll: LinkedList) -> LinkedList.Node:
    """
    Time: O(n)
    Space: O(1)
    >>> ll = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)
    >>> tail = ll.node_at(-1)
    >>> tail.next = ll.node_at(3)
    >>> loop_beginning(ll).val
    4
    >>> ll = LinkedList(1, 2)
    >>> tail = ll.node_at(-1)
    >>> tail.next = ll.node_at(0)
    >>> loop_beginning(ll).val
    1
    >>> ll = LinkedList(1)
    >>> tail = ll.node_at(-1)
    >>> tail.next = ll.node_at(0)
    >>> loop_beginning(ll).val
    1
    >>> ll = LinkedList(1, 2, 3)
    >>> tail = ll.node_at(-1)
    >>> tail.next = ll.node_at(-1)
    >>> loop_beginning(ll).val
    3
    """

    slow = ll.head.next
    fast = slow.next
    if fast.next is slow:
        return fast
    x = 2
    while slow is not fast:
        slow = slow.next
        fast = fast.next.next
        x += 1
    fast = fast.next
    y = 2
    while fast is not slow:
        fast = fast.next
        y += 1
    slow = ll.head
    x += y
    y = 0
    while y != x:
        slow = slow.next
        y += 1
    return slow.next

doctest.testmod()
