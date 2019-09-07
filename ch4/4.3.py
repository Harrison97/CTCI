import doctest
from collections import deque

import Tree
import LinkedList

Tree = Tree.Tree
LinkedList = LinkedList.SinglyLinkedList

def get_levels(t: Tree) -> [LinkedList]:
    """
    Complexity: O(2^depth) or O(nodes) on space and time
    Doing recursive w DFS would be same time but O(d) space!!!
    >>> t = Tree()
    >>> t.bst_from([1, 2, 3])
    >>> get_levels(t)
    [[2], [1, 3]]
    >>> t.bst_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> get_levels(t)
    [[5], [3, 8], [2, 4, 7, 9], [1, 6]]
    """

    if not t.root:
        return []
    n = t.root
    n.level = 0
    q = deque([n])
    levels = [LinkedList()]
    while q:
        n = q.popleft()
        if n.left:
            n.left.level = n.level + 1
            q.append(n.left)
        if n.right:
            n.right.level = n.level + 1
            q.append(n.right)

        levels[n.level].append_to_tail(n.data)
        if q and n.level != q[0].level:
            levels.append(LinkedList())
    return levels

doctest.testmod()

