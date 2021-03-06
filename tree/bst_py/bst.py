'''

BINARY SEARCH TREE

Description:    Binary search tree immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        (update later)

'''


from binnode import BinNode


class BinarySearchTree:
    '''
    Binary search tree.

    Args:
        lst: The list to construct from. If lst if None, the tree is empty.
        candd_removal: Candidate chosen for replacement when doing "remove" action. This argument can be "left" or "right".
    '''
    #
    #
    def __init__(self, lst: list = None, candd_removal='right'):
        self.root = None

        if candd_removal not in ('left', 'right'):
            raise ValueError('Invalid argument: candd_removal')

        self.__option_candidate_removal = candd_removal

        self.__count = 0

        if lst is not None:
            self.__construct_from_list(lst)

    #
    #
    def count(self):
        '''
        Returns number of elements.
        '''
        return self.__count

    #
    #
    def __count_traversal(self, node):
        '''
        Counts number of elements by traversal.
        '''
        if node is None:
            return 0

        count_le = self.__count_traversal(node.left)
        count_ri = self.__count_traversal(node.right)

        res = count_le + count_ri
        return res

    #
    #
    def traverse(self, order='in'):
        '''
        Traverses tree entirely.
        Args:
            order: Type of traversal order.
                - 'pre': pre-order
                - 'in': in-order
                - 'post': post-order
        Returns:
            A list of keys.
        '''

        if order not in ('pre', 'in', 'post'):
            raise ValueError('Invalid argument: order')

        self.__res_traveral = []

        if order == 'pre':
            self.__traverse_pre(self.root)
        elif order == 'in':
            self.__traverse_in(self.root)
        elif order == 'post':
            self.__traverse_post(self.root)

        res = self.__res_traveral
        del self.__res_traveral

        return res

    #
    #
    def __traverse_pre(self, node: BinNode):
        if node is None:
            return

        self.__res_traveral.append(node.key)
        self.__traverse_pre(node.left)
        self.__traverse_pre(node.right)

    #
    #
    def __traverse_in(self, node: BinNode):
        if node is None:
            return

        self.__traverse_in(node.left)
        self.__res_traveral.append(node.key)
        self.__traverse_in(node.right)

    #
    #
    def __traverse_post(self, node: BinNode):
        if node is None:
            return

        self.__traverse_post(node.left)
        self.__traverse_post(node.right)
        self.__res_traveral.append(node.key)

    #
    #
    def __str__(self):
        traversal_res = self.traverse()
        res = '  '.join(str(x) for x in traversal_res)
        res = f'BST({res})'
        return res

    #
    #
    def depth_level(self):
        '''
        Gets depth level of the tree.
        '''
        return self.__depth_level(self.root)

    #
    #
    def __depth_level(self, node: BinNode):
        if node is None:
            return 0

        depth_left_branch = 1 + self.__depth_level(node.left)
        depth_right_branch = 1 + self.__depth_level(node.right)

        return max(depth_left_branch, depth_right_branch)

    #
    #
    def search(self, key):
        '''
        Searches for a key.
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

        return (None, None)  # ensure a value to return, unreachable statement...

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
            self.__count += 1
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
        node, parent = self.__search(self.root, key)

        if node is None:
            return False

        self.__remove_node(node, parent)
        self.__count -= 1

        return True

    #
    #
    def __remove_node(self, node, parent):
        '''
        Removes the node from the tree.
        Args:
            node: The node to be removed.
            parent: The node's parent.
        Returns:
            None.
        '''

        have_left_child, have_right_child = node.left is not None, node.right is not None

        if have_left_child and have_right_child:
            candidate, candidate_pa = self.__get_candidate_removal(node)
            node.key = candidate.key
            self.__remove_node(candidate, candidate_pa)

        elif have_left_child:
            node.assign(node.left)

        elif have_right_child:
            node.assign(node.right)

        else:
            # node is leaf and does not have any children
            if parent is not None:
                parent.remove_child(node)
            else:
                # node has no parent, so that node is the root of the tree
                self.root = None

    #
    #
    def __get_candidate_removal(self, node):
        '''
        Gets a candidate for replacement. This is the helper function for "remove node" action.
        Args:
            node: The starting node.
        Returns:
            The tuple (node, parent) indicating result node and its parent.
        '''
        option = self.__option_candidate_removal

        if option == 'right':
            return self.__search_min(node.right, node)
        elif option == 'left':
            return self.__search_max(node.left, node)

        raise ValueError('Invalid __option_candidate_removal')

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
    def __construct_from_list(self, lst: list):
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

        self.root = self.__construct_from_sorted_list(lst, 0, len_lst - 1)
        self.__count = self.__count_traversal(self.root)

    #
    #
    def __construct_from_sorted_list(self, lst: list, start_idx: int, end_idx: int):
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
        root_node = BinNode(lst[mid_idx])

        root_node.left = self.__construct_from_sorted_list(lst, start_idx, mid_idx - 1)
        root_node.right = self.__construct_from_sorted_list(lst, mid_idx + 1, end_idx)

        return root_node
