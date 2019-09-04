import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

# Could also be done with 2 points, one stating k nodes behind the other.
# Return the slow node when the fast node reaches the end.
# This is the same Time and Space Complexity as the function below.
def get_kth_last_element(ll: LinkedList, k: int) -> int:
    """
    A function to get the kth to lsat element in a singly linked list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    >>> get_kth_last_element(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 2)
    7
    >>> get_kth_last_element(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 1)
    8
    >>> get_kth_last_element(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 0)
    >>> get_kth_last_element(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 8)
    1
    >>> get_kth_last_element(LinkedList(1, 2, 3, 4, 5, 6, 7, 8), 9)
    """

    if k < 1:
        return None

    curr_node = ll.head
    length = 0
    while curr_node:
        length += 1
        curr_node = curr_node.next
    if k > length:
        return None
    curr_node = ll.head
    curr_index = 0
    while curr_node:
        if curr_index == length - k:
            return curr_node.val
        curr_node = curr_node.next
        curr_index += 1

    return None

doctest.testmod()
