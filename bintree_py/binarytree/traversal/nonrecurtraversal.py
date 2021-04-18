from collections import deque
from .itraversal import ITraversal


#
#
class NonRecurTraversal(ITraversal):
    #
    #
    def traverse(self, root, order: str) -> list:
        if order not in ('pre', 'in', 'post'):
            raise ValueError('Invalid argument: order')

        res_path = []

        if root is None:
            return res_path

        if order == 'pre':
            res_path = self._traverse_pre(root)

        elif order == 'in':
            res_path = self._traverse_in(root)

        elif order == 'post':
            res_path = self._traverse_post(root)

        return res_path

    #
    #
    def _traverse_pre(self, node):
        res_path = []
        stack = deque()

        stack.append(node)

        while stack:
            node = stack.pop()
            res_path.append(node.key)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)

        return res_path

    #
    #
    def _traverse_post(self, node):
        res_path = []
        stack = deque()

        stack.append(node)

        while stack:
            node = stack.pop()
            res_path.append(node.key)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        return res_path[::-1]

    #
    #
    def _traverse_in(self, node):
        res_path = []
        stack = deque()

        while True:
            while node is not None:
                stack.append(node)
                node = node.left

            if not stack:
                break

            picked_node = stack.pop()
            res_path.append(picked_node.key)

            node = picked_node.right

        return res_path
