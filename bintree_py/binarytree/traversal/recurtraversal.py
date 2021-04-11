from .basetraversal import BaseTraversal


#
#
class RecurTraversal(BaseTraversal):
    #
    #
    def traverse(self, root, order: str) -> list:
        if order not in ('pre', 'in', 'post'):
            raise ValueError('Invalid argument: order')

        self._res_path = []

        if order == 'pre':
            self._traverse_pre(root)

        elif order == 'in':
            self._traverse_in(root)

        elif order == 'post':
            self._traverse_post(root)

        res = self._res_path
        del self._res_path

        return res

    #
    #
    def _traverse_pre(self, node):
        if node is None:
            return

        self._res_path.append(node.key)
        self._traverse_pre(node.left)
        self._traverse_pre(node.right)

    #
    #
    def _traverse_in(self, node):
        if node is None:
            return

        self._traverse_in(node.left)
        self._res_path.append(node.key)
        self._traverse_in(node.right)

    #
    #
    def _traverse_post(self, node):
        if node is None:
            return

        self._traverse_post(node.left)
        self._traverse_post(node.right)
        self._res_path.append(node.key)
