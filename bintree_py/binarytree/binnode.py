class BinNode:
    '''
    Binary Node.

    Args:
        key: The key stored in the node.
    '''
    #
    #
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    #
    #
    def __str__(self):
        return str(self.key)

    #
    #
    def assign(self, other_node: 'BinNode'):
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
