'''

BINARY SEARCH TREE

Description:    Binary search tree implementation

'''


from .binnode import BinNode
from .bintree import BinTree


#
#
class BinSearchTree(BinTree):
    '''
    Binary Search Tree.

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
        super().__init__()

        self._size = 0

        if lst is not None and type(lst) is not list:
            raise ValueError('Invalid argument: lst must be a list')

        if canddrm not in ('left', 'right'):
            raise ValueError('Invalid argument: canddrm')

        self._option_candd_rm = canddrm

        if lst is not None:
            self._construct_from_list(lst)

    #
    #
    def size(self):
        '''
        Returns number of nodes.
        '''
        return self._size

    #
    #
    def contain(self, key):
        '''
        Checks if key exists.

        Args:
            key: The key to search for.

        Returns:
            True if key exists. Otherwise, None.
        '''
        if key is None:
            raise ValueError('Invalid argument: key must not be None')

        node, _ = self._search(self._root, key)
        return node is not None

    #
    #
    def insert(self, key):
        '''
        Inserts a key.

        Args:
            key: The key to insert.

        Returns:
            If insertion succeeds, return True. Otherwise, rerturn False.
        '''
        if key is None:
            raise ValueError('Invalid argument: key must not be None')

        self._success_state = False

        self._root = self._insert(self._root, key)

        if self._success_state is False:
            del self._success_state
            return False

        self._size += 1

        del self._success_state
        return True

    #
    #
    def remove(self, key):
        '''
        Removes the node of given key.

        Args:
            key: The key to be removed.

        Returns:
            If key exists, return True. Otherwise, rerturn False.
        '''
        if key is None:
            raise ValueError('Invalid argument: key must not be None')

        if self._root is None:
            return False

        if self.contain(key) is False:
            return False

        self._root = self._remove(self._root, key)

        self._size -= 1
        return True

    #
    #
    def min(self):
        '''
        Searches for minimum key.

        Returns:
            Minimum key if exists. Otherwise, None.
        '''
        node, _ = self._search_min(self._root, None)
        res = node.key if node is not None else None
        return res

    #
    #
    def max(self):
        '''
        Searches for maximum key.

        Returns:
            Maximum key if exists. Otherwise, None.
        '''
        node, _ = self._search_max(self._root, None)
        res = node.key if node is not None else None
        return res

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _insert(self, node: BinNode, key):
        '''
        Inserts a key (backend function).

        Args:
            node: Current processing node.
            key: The key to insert.

        Returns:
            The current processing node itself.
        '''
        if node is None:
            self._success_state = True
            return self._create_node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    #
    #
    def _remove(self, node: BinNode, key):
        '''
        Removes the node from the tree.

        Args:
            node: The current processing node.
            key: The key to search and remove.

        Returns:
            The current processing node itself.
        '''
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

        return node

    #
    #
    def _remove_candidate(self, node: BinNode):
        '''
        Finds a candidate for replacement of current node, and then removes that candidate from the tree.

        Args:
            node: The starting node.
        '''
        assert node is not None

        option = self._option_candd_rm

        if option == 'right':
            candidate, _ = self._search_min(node.right, node)
            node.key = candidate.key
            node.right = self._remove(node.right, candidate.key)

        elif option == 'left':
            candidate, _ = self._search_max(node.left, node)
            node.key = candidate.key
            node.left = self._remove(node.left, candidate.key)

    #
    #
    def _search(self, node: BinNode, key):
        '''
        Searches for a key.

        Args:
            key: The key to search for.

        Returns:
            The tuple (node, parent) indicating result node and its parent.
        '''
        parent = None

        while True:
            if node is None:
                return (None, None)

            if key == node.key:
                return (node, parent)

            parent = node

            if key < node.key:
                node = node.left
            else:
                node = node.right

        return (None, None)  # ensure a value to return, unreachable statement...

    #
    #
    def _search_min(self, node: BinNode, parent: BinNode):
        '''
        Searches for the node with minimum key.

        Args:
            node: Starting node.
            parent: Parent of starting node.

        Returns:
            The tuple (node, parent) indicating result node and its parent.
        '''
        if node is None:
            return (None, parent)

        while node.left is not None:
            parent = node
            node = node.left

        return (node, parent)

    #
    #
    def _search_max(self, node: BinNode, parent: BinNode):
        '''
        Searches for the node with maximum key.

        Args:
            node: Starting node.
            parent: Parent of starting node.

        Returns:
            The tuple (node, parent) indicating result node and its parent.
        '''
        if node is None:
            return (None, parent)

        while node.right is not None:
            parent = node
            node = node.right

        return (node, parent)

    #
    #
    def _construct_from_list(self, lst: list):
        '''
        Constructs tree from a list. WARNING: The list will change its value (i.e. sorting).

        Args:
            lst: The input list.

        Returns:
            None.
        '''
        self._dispose_root(self._root)
        self._root = None

        lst = sorted(set(lst))
        len_lst = len(lst)

        self._root = self._build_tree_from_sorted_list(lst, 0, len_lst - 1)
        self._count = len_lst

    #
    #
    def _build_tree_from_sorted_list(self, lst: list, index_start: int, index_end: int):
        '''
        Backend function for "_construct_from_list".

        Args:
            lst: The list.
            index_start: Starting index in list.
            index_end: Ending index in list (inclusive).

        Returns:
            Root node (followed by its branch) constructed from lst[ index_start to index_end ]
        '''
        if index_start > index_end:
            return None

        index_mid = (index_start + index_end) // 2
        node = self._create_node(lst[index_mid])

        node.left = self._build_tree_from_sorted_list(lst, index_start, index_mid - 1)
        node.right = self._build_tree_from_sorted_list(lst, index_mid + 1, index_end)

        self._build_tree_from_sorted_list_node_func(node)

        return node

    #
    #
    def _build_tree_from_sorted_list_node_func(self, node):
        pass

    #
    #
    #################################################################
    #                        METHODS (EXTRA)
    #################################################################
    #
    #
    def __str__(self):
        return 'BST' + self._get_traversal_str()
