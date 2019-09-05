import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList


# Time: O(n)
# Space: O(1)
def sum_list(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    >>> sum_list(LinkedList(7, 1, 6), LinkedList(5, 9, 2))
    [2, 1, 9]
    >>> sum_list(LinkedList(7, 1, 6), LinkedList(5, 9, 2, 1))
    [2, 1, 9, 1]
    >>> sum_list(LinkedList(5, 9, 2, 1), LinkedList(7, 1, 6))
    [2, 1, 9, 1]
    >>> sum_list(LinkedList(5), LinkedList(1))
    [6]
    """

    carry = 0
    curr1, curr2 = ll1.head, ll2.head
    while (curr1.next if curr1 else None) or \
            (curr2.next if curr2 else None):
        s = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
        carry = int(s/10)
        curr1 = append_to_node(s%10, curr1)
        curr2 = append_to_node(s%10, curr2)
    s = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
    carry = int(s/10)
    if curr1:
        curr1 = append_to_node(LinkedList.Node(carry), curr1, val=s%10)
        return ll1
    if curr2:
        curr2 = append_to_node(LinkedList.Node(carry), curr2, val=s%10)
        return ll2

def append_to_node(data, n: LinkedList.Node, val=None):
    if type(data) == int:
        n.val = data
        return n.next
    elif type(data) == LinkedList.Node:
        n.val = val
        n.next = data if data.val else None
        return data
    return None

doctest.testmod()
