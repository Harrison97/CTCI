import Tree

Tree = Tree.Tree

t = Tree()
t.bst_from([1, 3, 5, 6, 6, 6.5, 7, 8, 8, 9])
print('DFS: ', t.depth_first())

