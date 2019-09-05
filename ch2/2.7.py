import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

def intersects(ll1: LinkedList, ll2: LinkedList) -> bool:
    """
    Time: O(n)
    Space: O(1)
    >>> n = LinkedList.Node(99)
    >>> ll1 = LinkedList(1, 2, 3)
    >>> ll1.append_node_to_tail(n)
    >>> ll1.append_to_tail(6)
    >>> ll2 = LinkedList(1)
    >>> ll2.append_node_to_tail(n)
    >>> ll2.append_to_tail(6)
    >>> ll2.append_to_tail(0)
    >>> intersects(ll1, ll2)
    True
    >>> n = LinkedList.Node(0)
    >>> ll1 = LinkedList(1)
    >>> ll1.append_node_to_tail(n)
    >>> ll2 = LinkedList(1)
    >>> ll2.append_node_to_tail(n)
    >>> intersects(ll1, ll2)
    True
    >>> intersects(LinkedList(1, 2, 3, 4, 5, 4, 3), LinkedList(4, 3, 5, 4, 3, 4, 3))
    False
    """

    curr1 = ll1.head
    curr2 = ll2.head
    reverse(curr1)
    while curr2.next:
        curr2 = curr2.next
    if curr1 is curr2:
        return True
    return False

def intersects_2(ll1: LinkedList, ll2: LinkedList) -> bool:
    """
    Time: O(n)
    Space: O(1)
    >>> n1 = LinkedList.Node(99)
    >>> n2 = LinkedList.Node(1)
    >>> n3 = LinkedList.Node(4)
    >>> n4 = LinkedList.Node(6)
    >>> ll1 = LinkedList(1, 2, 3)
    >>> ll2 = LinkedList(1)
    >>> ll1.append_node_to_tail(n1)
    >>> ll1.append_node_to_tail(n2)
    >>> ll1.append_node_to_tail(n3)
    >>> ll1.append_node_to_tail(n4)
    >>> ll2.append_node_to_tail(n1)
    >>> intersects_2(ll1, ll2)
    99
    >>> n1 = LinkedList.Node(99)
    >>> n2 = LinkedList.Node(1)
    >>> ll1 = LinkedList(1, 2, 3)
    >>> ll2 = LinkedList(1, 2, 3, 5, 1, 2, 3, 4, 2, 3, 1)
    >>> ll1.append_node_to_tail(n1)
    >>> ll1.append_node_to_tail(n2)
    >>> ll2.append_node_to_tail(n1)
    >>> intersects_2(ll1, ll2)
    99
    >>> intersects_2(LinkedList(1, 2, 3, 4, 5, 4, 3), LinkedList(4, 3, 5, 4, 3, 4, 3))
    """

    curr1 = ll1.head
    curr2 = ll2.head
    length_1 = 1
    length_2 = 1

    while curr1.next:
        curr1 = curr1.next
        length_1 += 1

    while curr2.next:
        curr2 = curr2.next
        length_2 += 1

    if curr1 is not curr2:
        return None

    curr1 = ll1.head
    curr2 = ll2.head

    if length_1 > length_2:
        while length_1 != length_2:
            length_1 -= 1
            curr1 = curr1.next
    elif length_1 < length_2:
        while length_1 != length_2:
            length_2 -= 1
            curr2 = curr2.next
    while curr1 is not curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1.val

def reverse(n: LinkedList.Node) -> LinkedList.Node:
    if not n.next:
        return n
    curr = n
    temp1 = curr.next
    temp2 = temp1.next
    curr.next = None
    while temp2:
        temp1.next = curr
        curr = temp1
        temp1 = temp2
        temp2 = temp2.next
    temp1.next = curr
    return temp1

doctest.testmod()
