from collections import deque
import doctest

def equalize(bt, st, n):
    while bt and bt[-1] > n:
        st.append(bt.pop())
    while st and st[-1] < n:
        bt.append(st.pop())

def sort_stack(s):
    """
    Uses 2 extra stacks.
    Can be done with only one extra stack but requires a little more popping.
    >>> s = deque([1, 6, 3, 4, 9, 8, 7, 2])
    >>> sort_stack(s)
    deque([9, 8, 7, 6, 4, 3, 2, 1])
    """
    st = deque()
    bt = deque()
    while s:
        equalize(bt, st, s[-1])
        bt.append(s.pop())
    while bt:
        st.append(bt.pop())
    return st

doctest.testmod()
