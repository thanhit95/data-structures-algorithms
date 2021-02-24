'''

BINARY SEARCH TREE

Description:    binary search tree immplementation

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        (update later)

'''


from libbstnode import *


class BinarySearchTree:
    '''
    Binary search tree.

    Args:
        lst: The list to construct from. If lst is None, the tree is empty.
    Returns:
        None
    '''
    #
    #
    def __init__(self, lst: list = None):
        self.root = None

    #
    #
    def traverse(self, order='in'):
        '''
        Traverses entire tree.
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

        return self.__res_traveral

    #
    #
    def __traverse_pre(self, node: BstNode):
        if node is None:
            return

        self.__res_traveral.append(node.key)
        self.__traverse_pre(node.left)
        self.__traverse_pre(node.right)

    #
    #
    def __traverse_in(self, node: BstNode):
        if node is None:
            return

        self.__traverse_in(node.left)
        self.__res_traveral.append(node.key)
        self.__traverse_in(node.right)

    #
    #
    def __traverse_post(self, node: BstNode):
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
    def __search(self, node: BstNode, key):
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
    def __insert(self, node: BstNode, key):
        if node is None:
            return BstNode(key)

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
        if node.left is not None and node.right is not None:
            child, child_pa = self.__search_min(node.right, node)  # find the minimum-key child in right branch for replacement
            node.key = child.key
            self.__remove_node(child, child_pa)

        elif node.left is not None:
            node.assign(node.left)

        elif node.right is not None:
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
    def __search_min(self, start_node: BstNode, parent_node: BstNode):
        '''
        Searches for the node with minimum key.
        Args:
            start_node: Starting node.
            parent_node: Parent of starting node.
        Returns:
            The tuple (node, parent) indicating result node and its parent.
        '''
        if start_node is None:
            return (None, None)

        parent = parent_node
        node = start_node

        while node.left is not None:
            parent = node
            node = node.left

        return (node, parent)
