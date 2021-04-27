'''

BINARY TREE

Description:    Binary tree (base class) implementation

'''


import copy
from abc import ABC, abstractmethod
from .binnode import BinNode
from .traversal import RecurTraversal
from .bintreeiter import BinTreeIterIn
from binarytreedisp import BinTreeDisplay  # may remove this line to make Python happy


#
#
class BinTree(ABC):
    '''
    Binary Tree.
    '''
    #
    #
    #################################################################
    #                        CONSTRUCTOR
    #################################################################
    #
    #
    def __init__(self):
        self._root = None

    #
    #
    #################################################################
    #                        ABSTRACT METHODS
    #################################################################
    #
    #
    @abstractmethod
    def size(self):
        raise NotImplementedError()

    @abstractmethod
    def insert(self, key):
        raise NotImplementedError()

    @abstractmethod
    def remove(self, key):
        raise NotImplementedError()

    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
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
        self._dispose_root(self._root)
        self._root = None

    #
    #
    def traverse(self, order: str = 'in'):
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
    def _dispose_root(self, node: BinNode):
        '''
        Helps garbage collection free memory used by tree.
        Args:
            node: Input node.
        '''
        if node is None:
            return

        self._dispose_root(node.left)
        del node.left

        self._dispose_root(node.right)
        del node.right

        del node.key

    #
    #
    # Adapter method connecting BinTreeDisplay and BinTree
    def display(self, disp: BinTreeDisplay) -> str:
        res = disp.get(self._root)
        return res

    #
    #
    # Adapter method connecting BinTreeDisplay and BinTree
    def display_lst_rows(self, disp: BinTreeDisplay) -> list:
        res = disp.get_lst_rows(self._root)
        return res

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
