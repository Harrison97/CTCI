class Graph:
    class Node:
        def __init__(self, d, c):
            self.data = d # node data
            self.children = c # list of nodes

    def __init__(self):
        self.nodes = [] # list of Node objects

