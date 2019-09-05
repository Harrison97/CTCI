import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList


def delete_middle_1(ll: LinkedList, n: LinkedList.Node) -> LinkedList:
    """
    delete_middle_1(SinglyLinkedList, node_to_delete)

    Time Complexity: O(n)
    Space Complexity: O(1)

    >>> ll = LinkedList(1, 2, 3, 4, 5)
    >>> delete_middle_1(ll, ll.node_at(2))
    [1, 2, 4, 5]
    """

    while n.next.next:
        n.val = n.next.val
        n = n.next
    n.val = n.next.val
    n.next = None
    return ll

def delete_middle_2(ll: LinkedList, n: LinkedList.Node) -> LinkedList:
    """
    delete_middle_2(SinglyLinkedList, node_to_delete)

    Time Complexity: O(1)
    Space Complexity: O(1)

    >>> ll = LinkedList(1, 2, 3, 4, 5)
    >>> delete_middle_2(ll, ll.node_at(2))
    [1, 2, 4, 5]
    """

    n.val = n.next.val
    n.next = n.next.next

    return ll

doctest.testmod()
