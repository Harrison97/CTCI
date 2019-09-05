import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

def is_palindrome(ll: LinkedList) -> bool:
    """
    Time: O(n)
    Space: O(1)
    >>> is_palindrome(LinkedList(1, 2, 3, 4, 5, 4, 3, 2, 1))
    True
    >>> is_palindrome(LinkedList(1, 2, 3, 4, 5, 5, 4, 3, 2, 1))
    True
    >>> is_palindrome(LinkedList(1, 2, 3, 4, 5, 6, 4, 3, 2, 1))
    True
    >>> is_palindrome(LinkedList(1))
    True
    >>> is_palindrome(LinkedList(1, 1))
    True
    >>> is_palindrome(LinkedList(1, 2))
    False
    >>> is_palindrome(LinkedList(1, 1, 2, 4, 1, 4, 3))
    False
    """

    if not ll.head.next:
        return True
    middle = get_middle(ll)
    right = reverse(middle)
    left = ll.head
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

def get_middle(ll: LinkedList) -> LinkedList.Node:
    slow = ll.head
    fast = slow
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    return slow

def reverse(curr: LinkedList.Node) -> LinkedList.Node:
    if not curr.next:
        return curr
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
