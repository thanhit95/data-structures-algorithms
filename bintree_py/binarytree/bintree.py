'''

BINARY TREE

Description:    Binary tree (base class) implementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


import copy
from .binnode import BinNode
from .traversal import RecurTraversal
from .bintreeiter import BinTreeIterIn


#
#
class BinTree:
    '''
    Binary Tree.
    '''
    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
    #
    #
    def __init__(self):
        self._root = None

    #
    #
    def empty(self):
        return self._root is None

    #
    #
    def height(self):
        '''
        Gets height of the tree.
        '''
        return self._height(self._root)

    #
    #
    def clear(self):
        '''
        Clears tree completely.
        '''
        self._free_memory(self._root)
        self._root = None

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
        res = traversal.traverse(self._root, order)

        del traversal
        return res

    #
    #
    def clone(self):
        '''
        Clones tree completely.
        '''
        the_clone = copy.deepcopy(self)
        return the_clone

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _height(self, node: BinNode):
        if node is None:
            return 0

        height_le = self._height(node.left)
        height_ri = self._height(node.right)

        return 1 + max(height_le, height_ri)

    #
    #
    def _create_node(self, key=None):
        return BinNode(key)

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
    #################################################################
    #                        METHODS (EXTRA)
    #################################################################
    #
    #
    def __str__(self):
        lst_traversal = self.traverse('in')
        res = '  '.join(str(x) for x in lst_traversal)
        res = f'({res})'
        return res

    #
    #
    def __iter__(self):
        return BinTreeIterIn(self)
