from .binnode import BinNode


#
#
class AvlNode(BinNode):
    '''
    AVL Node.

    Args:
        key: The key stored in the node.
    '''
    #
    #
    def __init__(self, key=None):
        super().__init__(key)
        self._height = 1

    #
    #
    def height(self):
        return self._height

    #
    #
    def height_left(self):
        return 0 if self.left is None else self.left.height()

    #
    #
    def height_right(self):
        return 0 if self.right is None else self.right.height()

    #
    #
    def update_height(self):
        self._height = 1 + max(self.height_left(), self.height_right())

    #
    #
    def balance(self):
        '''
        Gets balance factor of the node.
        '''
        height_le = self.height_left()
        height_ri = self.height_right()
        return height_le - height_ri

    #
    #
    def balance_left(self):
        '''
        Gets balance factor of the left branch.
        '''
        return 0 if self.left is None else self.left.balance()

    #
    #
    def balance_right(self):
        '''
        Gets balance factor of the right branch.
        '''
        return 0 if self.right is None else self.right.balance()
