'''

AVL TREE

Description:    AVL tree immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


from .bst import BinarySearchTree
from .avlnode import AvlNode


#
#
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
    def _insert(self, node: AvlNode, key):
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
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        # Step 2. Adjusts balance
        node = self.__adjust_balance(node)
        return node

    #
    #
    def _remove(self, node: AvlNode, key):
        '''
        Removes the node from the tree.
        Args:
            node: The current processing node.
            key: The key to search and remove.
        Returns:
            The node (root) itself.
        '''

        # Step 1. Performs normal BST
        if node is None:
            return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            self._remove_candidate(node)

        # Step 2. Adjusts balance
        node = self.__adjust_balance(node)
        return node

    #
    #
    def __adjust_balance(self, node: AvlNode):
        # STEP 1. Updates the height of the node
        node.update_height()

        # STEP 2. Gets the balance factor
        balance = node.balance()
        balance_le = node.balance_left()
        balance_ri = node.balance_right()

        # STEP 3. Processes if the node is unbalanced ==> 4 cases

        # Case 1: left-left
        if balance > 1 and balance_le >= 0:
            return self.__rotate_right(node)

        # Case 2: right-right
        if balance < -1 and balance_ri <= 0:
            return self.__rotate_left(node)

        # Case 3: left-right
        if balance > 1 and balance_le < 0:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        # Case 4: right-left
        if balance < -1 and balance_ri > 0:
            node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node

    #
    #
    def __rotate_left(self, node: AvlNode):
        r'''
            node
            /  \
           ..   V
               / \
              a   b
        '''
        V = node.right
        a = V.left

        V.left = node
        node.right = a

        node.update_height()
        V.update_height()

        return V

    #
    #
    def __rotate_right(self, node: AvlNode):
        r'''
            node
            /  \
           V   ..
          / \
         a   b
        '''
        V = node.left
        b = V.right

        V.right = node
        node.left = b

        node.update_height()
        V.update_height()

        return V

    #
    #
    def _create_node(self, key=None):
        return AvlNode(key)

    #
    #
    def __str__(self):
        lst_traversal = self.traverse()
        res = '  '.join(str(x) for x in lst_traversal)
        res = f'AVL({res})'
        return res