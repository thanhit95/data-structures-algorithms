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
        height = self.__depth_level * 2 - 1

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

        width_left_branch, size_left_dash, size_right_dash \
            = node.width_left_branch, node.size_left_dash, node.size_right_dash

        margin = margin_global + width_left_branch + size_left_dash

        self.__buffer.fill(margin, depth * 2 - 2, node.key)

        if node.left is not None or node.right is not None:
            self.__buffer.fill(margin, depth * 2 - 1, '|')

        self.__fill_matrix(node.left, depth + 1, margin_global)
        self.__fill_matrix(node.right, depth + 1, margin + 1 + size_right_dash)

        if node.left is not None:
            self.__fill_horizontal_dash(margin, depth * 2, 'left')

        if node.right is not None:
            self.__fill_horizontal_dash(margin, depth * 2, 'right')

    #
    #
    def __fill_horizontal_dash(self, posx, posy, direction):
        buffer = self.__buffer
        a = buffer.a
        dash = self.__parser.dash

        if direction == 'left':
            if a[posy][posx] == dash:
                posx -= 1

            for x in range(posx, -1, -1):
                if a[posy][x] == ' ':
                    a[posy][x] = dash
                else:
                    break

        elif direction == 'right':
            if a[posy][posx] == dash:
                posx += 1

            for x in range(posx, buffer.width):
                if a[posy][x] == ' ':
                    a[posy][x] = dash
                else:
                    break

        else:
            raise ValueError('Invalid argument: direction')
