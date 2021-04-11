'''

BINARY TREE

Description:    Binary tree (base class) immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


import copy
from .binnode import BinNode
from .bintreeiter import BinTreeIterIn
from .traversal import RecurTraversal


#
#
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
    def clear(self):
        '''
        Clears tree completely.
        '''
        self._free_memory(self.root)
        self.root = None

    #
    #
    def clone(self):
        '''
        Clones tree completely.
        '''
        tree = copy.copy(self)
        tree.root = tree._clone(tree.root)
        return tree

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
        Traverses the tree entirely.
        Args:
            order: Type of traversal order.
                - 'pre': pre-order
                - 'in': in-order
                - 'post': post-order
        Returns:
            A list of keys.
        '''
        traversal = RecurTraversal()
        res = traversal.traverse(self.root, order)

        del traversal
        return res

    #
    #
    def _clone(self, node_src):
        '''
        Clones the tree.
        Args:
            node_src: Source node.
        '''
        if node_src is None:
            return None

        node = copy.copy(node_src)
        node.left = self._clone(node.left)
        node.right = self._clone(node.right)

        return node

    #
    #
    def _free_memory(self, node: BinNode):
        '''
        Helps garbage collection free memory used by tree.
        Args:
            node: Input node.
        '''
        if node is None:
            return

        self._free_memory(node.left)
        self._free_memory(node.right)

        del node.left
        del node.right

    #
    #
    def __height(self, node: BinNode):
        if node is None:
            return 0

        height_le = self.__height(node.left)
        height_ri = self.__height(node.right)

        return 1 + max(height_le, height_ri)

    #
    #
    def __iter__(self):
        return BinTreeIterIn(self)
