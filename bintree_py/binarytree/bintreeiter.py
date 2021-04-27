class BinTreeIterIn:
    '''
    Binary Tree Interator.

    This class uses in-order traversal.
    '''
    def __init__(self, tree):
        self.__tree = tree
        self.__stack = []
        self.__node = tree._root

    #
    #
    def __next__(self):
        stack = self.__stack
        node = self.__node

        while node is not None:
            stack.append(node)
            node = node.left

        if not stack:
            raise StopIteration()

        res_node = stack.pop()
        self.__node = res_node.right

        del stack
        del node

        return res_node.key
