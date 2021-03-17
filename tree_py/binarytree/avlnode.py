from .binnode import BinNode


class AvlNode(BinNode):
    #
    #
    def __init__(self, key=None):
        super().__init__(key)
        self.__height = 1

    #
    #
    def height(self):
        return self.__height

    #
    #
    def update_height(self):
        self.__height = 1 + max(self.__height_child(self.left), self.__height_child(self.right))

    #
    #
    def balance(self):
        '''
        Gets balance factor of the node.
        '''
        height_le = self.__height_child(self.left)
        height_ri = self.__height_child(self.right)
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

    #
    #
    def __height_child(self, child):
        return 0 if child is None else child.height()
