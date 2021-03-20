'''

BINARY SEARCH TREE

Description:    Binary search tree immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        MIT

'''


from .binnode import BinNode
from .bintree import BinTree


class BinarySearchTree(BinTree):
    '''
    Binary Search Tree.

    Args:
        lst: The list to construct from. If lst if None, the tree is empty.
        candd_removal: Candidate chosen for replacement when doing "remove" action. This argument can be "left" or "right".
    '''
    #
    #
    def __init__(self, lst: list = None, candd_removal='right'):
        super().__init__()

        self._count = 0

        if candd_removal not in ('left', 'right'):
            raise ValueError('Invalid argument: candd_removal')

        self.__option_candidate_removal = candd_removal

        if lst is not None:
            self.construct_from_list(lst)

    #
    #
    def count(self):
        '''
        Returns number of elements.
        '''
        return self._count

    #
    #
    def get(self, key):
        '''
        Gets a node of given key.
        Args:
            key: The key to search for.
        Returns:
            The node containing the key, if found. Otherwise, None.
        '''
        res, _ = self.__search(self.root, key)
        return res

    #
    #
    def __search(self, node: BinNode, key):
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

        return (None, None)  # ensures a value to return, unreachable statement...

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
    def __insert(self, node: BinNode, key):
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
            return BinNode(key)

        if key < node.key:
            node.left = self.__insert(node.left, key)
        elif key > node.key:
            node.right = self.__insert(node.right, key)

        return node

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
        if self.root is None:
            return False

        self.root = self.__remove(self.root, key)

        self._count -= 1

        return True

    #
    #
    def __remove(self, node: BinNode, key):
        '''
        Removes the node from the tree.
        Args:
            node: The current processing node.
            key: The key to search and remove.
        Returns:
            The node (root) itself.
        '''

        if node is None:
            return None

        if key < node.key:
            node.left = self.__remove(node.left, key)
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                self._remove_candidate(node, self.__remove)

        return node

    #
    #
    def _remove_candidate(self, node: BinNode, fn_remove):
        '''
        Finds a candidate for replacement of current node, and then removes that candidate from the tree.
        Args:
            node: The starting node.
        Returns:
            None.
        '''
        option = self.__option_candidate_removal

        if option == 'right':
            candidate, _ = self.__search_min(node.right, node)
            node.key = candidate.key
            node.right = fn_remove(node.right, candidate.key)

        elif option == 'left':
            candidate, _ = self.__search_max(node.left, node)
            node.key = candidate.key
            node.left = fn_remove(node.left, candidate.key)

    #
    #
    def __search_min(self, node: BinNode, parent: BinNode):
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
    def __search_max(self, node: BinNode, parent: BinNode):
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
    def min(self):
        '''
        Searches for minimum key.
        Args:
            None.
        Returns:
            Minimum key if exists. Otherwise, None.
        '''
        node, _ = self.__search_min(self.root, None)
        res = node.key if node is not None else None
        return res

    #
    #
    def max(self):
        '''
        Searches for maximum key.
        Args:
            None.
        Returns:
            Maximum key if exists. Otherwise, None.
        '''
        node, _ = self.__search_max(self.root, None)
        res = node.key if node is not None else None
        return res

    #
    #
    def construct_from_list(self, lst: list):
        '''
        Constructs tree from a list. WARNING: The list will change its value (i.e. sorting).
        Args:
            lst: The list.
        Returns:
            None.
        '''
        self.root = None
        lst.sort()
        len_lst = len(lst)

        self.root = self._construct_from_sorted_list(lst, 0, len_lst - 1)
        self._count = self._count_traversal(self.root)

    #
    #
    def _construct_from_sorted_list(self, lst: list, start_idx: int, end_idx: int):
        '''
        Backend function for "__construct_from_list".
        Args:
            lst: The list.
            start_idx: Starting index in list.
            end_idx: Ending index in list (inclusive).
        Returns:
            Root node (followed by its branch) constructed from lst[ start_idx to end_idx ]
        '''

        if start_idx > end_idx:
            return None

        mid_idx = (start_idx + end_idx) // 2
        # node = BinNode(lst[mid_idx])
        node = self._create_node(lst[mid_idx])

        node.left = self._construct_from_sorted_list(lst, start_idx, mid_idx - 1)
        node.right = self._construct_from_sorted_list(lst, mid_idx + 1, end_idx)

        return node

    #
    #
    def _create_node(self, key=None):
        return BinNode(key)

    #
    #
    def __str__(self):
        lst_traversal = self.traverse()
        res = '  '.join(str(x) for x in lst_traversal)
        res = f'BST({res})'
        return res
