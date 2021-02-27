'''

BINARY SEARCH TREE DISPLAYER

Description:    This tool visualizes binary tree by drawing.

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        (update later)

'''


from binnode import BinNode
from bst import BinarySearchTree
from bintreedisplayparser import ValueUtil, BinTreeDisplayParser
from matrixbuffer import MatrixBuffer


class BinTreeDisplay:
    '''
    Binary tree displayer. This tool visualizes binary tree by drawing.
    '''
    #
    #
    def __init__(self):
        self.__vutil = ValueUtil()
        self.__parser = BinTreeDisplayParser(self.__vutil)

    #
    #
    def get_str(self, bst: BinarySearchTree, dash: str = '-', dash_size: int = 3):
        '''
        Gets display string for binary search tree.
        Args:
            bst: Input binary search tree.
            dash: Dash character. The term "dash" means a horizontal line connecting left and right leaves.
            dash_size: Dash size (the length between left and right leaves).
        Returns:
            String result.
        '''
        self.__parser.config_dash(dash, dash_size)

        self.__depth_level = bst.depth_level()
        height = self.__depth_level * 3 - 2

        parser_tree = self.__parser.build_tree(bst.root)

        self.__buffer = MatrixBuffer(parser_tree.width, height)

        self.__fill_matrix(parser_tree, 1, 0)

        matrix = self.__buffer
        del self.__depth_level
        del self.__buffer

        return matrix.get_str()

    #
    #
    def __fill_matrix(self, node: BinNode, depth: int, margin_global: int):
        if node is None:
            return

        margin_key = margin_global + node.margin_key
        margin_left = margin_global + node.margin_left_child
        margin_right = margin_global + node.margin_right_child
        margin_global_right = margin_key + 1 + node.size_right_dash

        self.__buffer.fill(margin_key, depth * 3 - 3, node.key)

        if node.left is not None or node.right is not None:
            self.__buffer.fill(margin_key, depth * 3 - 2, '|')

        if node.left is not None:
            self.__fill_dash('left', node.left.key, depth * 3 - 1, margin_left, margin_key)
            self.__fill_matrix(node.left, depth + 1, margin_global)

        if node.right is not None:
            self.__fill_dash('right', node.right.key, depth * 3 - 1, margin_key, margin_right)
            self.__fill_matrix(node.right, depth + 1, margin_global_right)

    #
    #
    def __fill_dash(self, direction: str, child_key: str, y, margin_a, margin_b):
        if direction == 'right':
            self.__fill_dash_coord(y, margin_a, margin_b)

        elif direction == 'left':
            margin_a += len(child_key) - 1
            self.__fill_dash_coord(y, margin_a, margin_b)

        else:
            raise ValueError('Invalid argument: direction')

    #
    #
    def __fill_dash_coord(self, y, startx, endx):
        a = self.__buffer.a
        dash = self.__parser.dash

        for x in range(startx, endx + 1):
            a[y][x] = dash
