"""
    From: https://github.com/aimacode/aima-python/blob/master/search.py
"""

class Node:
    def __init__(self, state=None, parent=None, depth=0, h_val=0):
        self.state = state
        self.parent = parent
        self.h_val = h_val
        self.depth = depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.depth + self.h_val < node.depth + node.h_val

    def __gt__(self, node):
        return self.depth + self.h_val > node.depth + node.h_val

    def __eq__(self, node):
        return self.depth + self.h_val == node.depth + node.h_val

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))