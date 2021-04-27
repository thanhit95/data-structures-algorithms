'''

AVL TREE

Description:    AVL tree implementation

'''


from .binsearchtree import BinSearchTree
from .avlnode import AvlNode


#
#
class AvlTree(BinSearchTree):
    '''
    AVL Tree.

    Args:
        lst: The list to construct from. If lst if None, the tree is empty.
        canddrm: Candidate chosen for replacement when doing "remove" action. This argument can be "left" or "right".
    '''
    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
    #
    #
    def __init__(self, lst: list = None, canddrm: str = 'right'):
        super().__init__(lst, canddrm)

    #
    #
    def height(self):
        '''
        Gets height of the tree.
        '''
        if self._root is None:
            return 0

        return self._root.height()

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _insert(self, node: AvlNode, key):
        '''
        Inserts a key (backend function).

        Args:
            node: Current processing node.
            key: The key to insert.

        Returns:
            The current processing node itself.
        '''
        node = super()._insert(node, key)
        node = self._adjust_balance(node)
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
            The current processing node itself.
        '''
        node = super()._remove(node, key)

        if node is not None:
            node = self._adjust_balance(node)

        return node

    #
    #
    def _adjust_balance(self, node: AvlNode):
        # STEP 1. Update the height of the node
        node.update_height()

        # STEP 2. Get the balance factor
        balance = node.balance()
        balance_le = node.balance_left()
        balance_ri = node.balance_right()

        # STEP 3. Process if the node is unbalanced ==> 4 cases

        # Case 1: left-left
        if balance > 1 and balance_le >= 0:
            return self._rotate_right(node)

        # Case 2: right-right
        if balance < -1 and balance_ri <= 0:
            return self._rotate_left(node)

        # Case 3: left-right
        if balance > 1 and balance_le < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Case 4: right-left
        if balance < -1 and balance_ri > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    #
    #
    def _rotate_left(self, node: AvlNode):
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
    def _rotate_right(self, node: AvlNode):
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
    def _build_tree_from_sorted_list_node_func(self, node: AvlNode):
        node.update_height()

    #
    #
    ################################################################
    #                        METHOD (EXTRA)
    ################################################################
    #
    #
    def __str__(self):
        return 'AVL' + self._get_traversal_str()
