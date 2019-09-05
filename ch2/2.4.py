import doctest
import LinkedList

LinkedList = LinkedList.SinglyLinkedList

# TC: O(n)
# SC: O(n)
# Bad implemintation
# Could be a little better if we kept trak of front oly nd appended to front of lists.
def partition(ll: LinkedList, x: int) -> LinkedList:
    """
    Time: O(n)
    Space: O(n)
    >>> partition(LinkedList(1, 2, 3, 5, 24, 2 ,567, 3, 45, 0), 20)
    [1, 2, 3, 5, 2, 3, 0, 24, 567, 45]
    >>> partition(LinkedList(1, 2, 10, 5, 1, 0, 8, 12, 4), 5)
    [1, 2, 1, 0, 4, 10, 5, 8, 12]
    """
    curr = ll.head
    ll_low = None
    ll_high = None
    last_low = None
    last_high = None
    while curr:
        if curr.val >= x:
            if not ll_high:
                ll_high = LinkedList.Node(curr.val)
                last_high = ll_high
            else:
                last_high.next = LinkedList.Node(curr.val)
                last_high = last_high.next
        else:
            if not ll_low:
                ll_low = LinkedList.Node(curr.val)
                last_low = ll_low
            else:
                last_low.next = LinkedList.Node(curr.val)
                last_low = last_low.next
        curr = curr.next

    partitioned = None
    if last_low:
        last_low.next = ll_high
        partitioned = ll_low
    else:
        partitioned = ll_high

    curr = partitioned
    ans = []
    while curr:
        ans.append(curr.val)
        curr = curr.next
    return LinkedList(ans)


doctest.testmod()
