'''

BINARY TREE

Description:    Binary tree (base class) immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        MIT

'''


from .binnode import BinNode
from .bintreeiter import BinTreeIterIn


class BinTree:
    '''
    Binary Tree.
    '''
    #
    #
    def __init__(self):
        self.root = None

    #
    #
    def empty(self):
        return self.root is None

    #
    #
    def height(self):
        '''
        Gets height of the tree.
        '''
        return self.__height(self.root)

    #
    #
    def _count_traversal(self, node: BinNode):
        '''
        Counts number of elements by traversal.
        '''
        if node is None:
            return 0

        count_le = self._count_traversal(node.left)
        count_ri = self._count_traversal(node.right)

        res = count_le + count_ri
        return res

    #
    #
    def traverse(self, order='in'):
        '''
        Traverses tree entirely.
        Args:
            order: Type of traversal order.
                - 'pre': pre-order
                - 'in': in-order
                - 'post': post-order
        Returns:
            A list of keys.
        '''

        if order not in ('pre', 'in', 'post'):
            raise ValueError('Invalid argument: order')

        self.__res_traveral = []

        if order == 'pre':
            self.__traverse_pre(self.root)
        elif order == 'in':
            self.__traverse_in(self.root)
        elif order == 'post':
            self.__traverse_post(self.root)

        res = self.__res_traveral
        del self.__res_traveral

        return res

    #
    #
    def __traverse_pre(self, node: BinNode):
        if node is None:
            return

        self.__res_traveral.append(node.key)
        self.__traverse_pre(node.left)
        self.__traverse_pre(node.right)

    #
    #
    def __traverse_in(self, node: BinNode):
        if node is None:
            return

        self.__traverse_in(node.left)
        self.__res_traveral.append(node.key)
        self.__traverse_in(node.right)

    #
    #
    def __traverse_post(self, node: BinNode):
        if node is None:
            return

        self.__traverse_post(node.left)
        self.__traverse_post(node.right)
        self.__res_traveral.append(node.key)

    #
    #
    def __height(self, node: BinNode):
        if node is None:
            return 0

        height_le = 1 + self.__height(node.left)
        height_ri = 1 + self.__height(node.right)

        return max(height_le, height_ri)

    #
    #
    def __iter__(self):
        return BinTreeIterIn(self)
