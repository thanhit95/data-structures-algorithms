'''

BINARY TREE

Description:    Binary tree (base class) immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


from .binnode import BinNode
from .bintreeiter import BinTreeIterIn
from .traveler import TravelerRecur


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
        traveler = TravelerRecur()
        res = traveler.traverse(self.root, order)

        del traveler
        return res

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
