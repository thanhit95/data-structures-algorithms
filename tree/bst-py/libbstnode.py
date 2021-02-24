class BstNode:
    '''
    BST Node.

    Args:
        key: The key stored in the node.
    '''
    #
    #
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        if self.key is None:
            raise ValueError('Invalid argument: key cannot be None')

    #
    #
    def __str__(self):
        return str(self.key)

    #
    #
    def assign(self, other_node: 'BstNode'):
        '''
        Assigns current-node values from other-node values.
        Args:
            other_node: Other node.
        '''
        if other_node is None:
            raise ValueError('Invalid argument: other_node cannot be None')

        self.key = other_node.key
        self.left = other_node.left
        self.right = other_node.right

    #
    #
    def remove_child(self, child, new_child=None):
        '''
        Removes the child node (no recursive).
        Args:
            child: Child node to be removed.
        Returns:
            1 if child is on the left.
            2 if child is on the right.
            0 if child is not found.
        '''
        if self.left is child:
            self.left = None
            return 1
        elif self.right is child:
            self.right = None
            return 2

        return 0
