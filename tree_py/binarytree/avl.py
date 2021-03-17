'''

AVL TREE

Description:    AVL tree immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        MIT

'''


from .bst import BinarySearchTree
from .avlnode import AvlNode


class AvlTree(BinarySearchTree):
    '''
    AVL Tree.

    Args:
        lst: The list to construct from. If lst if None, the tree is empty.
        candd_removal: Candidate chosen for replacement when doing "remove" action. This argument can be "left" or "right".
    '''
    #
    #
    def __init__(self, lst: list = None, candd_removal='right'):
        super().__init__(lst=None, candd_removal=candd_removal)

        self._func_create_node = AvlTree.__create_node

        if lst is not None:
            self.construct_from_list(lst)

    #
    #
    def height(self):
        '''
        Gets height of the tree.
        '''
        if self.root is None:
            return 0

        return self.root.height()

    #
    #
    def insert(self, key):
        '''
        Inserts a key.
        Args:
            key: The key to insert.
        '''
        self.root = self.__insert(self.root, key)

    #
    #
    def __insert(self, node: AvlNode, key):
        '''
        Inserts a key (backend function)
        Args:
            node: Current processing node.
            key: The key to insert.
        Returns:
            The current processing node itself.
        '''
        if node is None:
            self._count += 1
            return AvlNode(key)

        # Step 1. Performs normal BST
        if key < node.key:
            node.left = self.__insert(node.left, key)
        elif key > node.key:
            node.right = self.__insert(node.right, key)

        # Step 2. Updates the height of the node
        node.update_height()

        # Step 3. Gets the balance factor
        balance = node.balance()

        # Step 4. Processes if the node is unbalanced ==> 4 cases

        # Case 1: left-left
        if balance > 1 and key < node.left.key:
            return self.__rotate_right(node)

        # Case 2: right-right
        if balance < -1 and key > node.right.key:
            return self.__rotate_left(node)

        # Case 3: left-right
        if balance > 1 and key > node.left.key:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        # Case 4: right-left
        if balance < -1 and key < node.right.key:
            node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node

    #
    #
    def __rotate_left(self, node: AvlNode):
        r'''
            node
            /  \
           ..   T
               / \
              a   b
        '''
        T = node.right
        a = T.left

        T.left = node
        node.right = a

        node.update_height()
        T.update_height()

        return T

    #
    #
    def __rotate_right(self, node: AvlNode):
        r'''
            node
            /  \
           T   ..
          / \
         a   b
        '''
        T = node.left
        b = T.right

        T.right = node
        node.left = b

        node.update_height()
        T.update_height()

        return T

    #
    #
    @staticmethod
    def __create_node(key=None):
        return AvlNode(key)

    #
    #
    def __str__(self):
        lst_traversal = self.traverse()
        res = '  '.join(str(x) for x in lst_traversal)
        res = f'AVL({res})'
        return res
