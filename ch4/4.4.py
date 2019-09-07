from collections import deque
import doctest

import Tree

Tree = Tree.Tree

def is_balanced(t: Tree) -> bool:
    """
    O(nodes)
    >>> t = Tree()
    >>> t.bst_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> is_balanced(t)
    True
    >>> t.bst_from([1, 2, 3, 4])
    >>> t.root.left.left.left = Tree.Node(0)
    >>> is_balanced(t)
    False
    """
    if not t.root:
        return True
    t.root.level = 0
    on_level = 1
    q = deque([t.root])
    while q:
        n = q.popleft()
        if n.left:
            n.left.level = n.level + 1
            q.append(n.left)
        if n.right:
            n.right.level = n.level + 1
            q.append(n.right)
        if q:
            if n.level == q[0].level:
                on_level += 1
            else:
                if on_level == 2**n.level:
                    on_level = 1
                else:
                    return False
    return True


doctest.testmod()
