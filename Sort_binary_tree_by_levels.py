#task: https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
import queue


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    res = []
    if node:
        q = queue.Queue()
        q.put(node)
        while not q.empty():
            current_node = q.get()
            res.append(current_node.value)
            if current_node.left:
                q.put(current_node.left)
            if current_node.right:
                q.put(current_node.right)
    return res


print(tree_by_levels(None)) # []
tree = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1) # [1, 2, 3, 4, 5, 6]
print(tree_by_levels(tree))