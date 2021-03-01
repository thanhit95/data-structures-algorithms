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
        self.config(('key', 'left', 'right'))

    #
    #
    def get(self, inp_root):
        '''
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            inp_struct_node, dash, dash_size, margin_left, float_format
        Args:
            inp_root: Input root of binary search tree.
        Returns:
            String result.
        '''
        buffer = self.__process(inp_root)
        return buffer.get_str()

    #
    #
    def get_lst_rows(self, inp_root):
        '''
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            inp_struct_node, dash, dash_size, margin_left, float_format
        Returns:
            List of rows. Each row is a string.
        '''
        buffer = self.__process(inp_root)
        return buffer.get_lst_rows()

    #
    #
    def __process(self, inp_root):
        '''
        Backend function for "get" method.
        '''

        self.__depth_level = self.__parser.get_depth_level(inp_root)
        height = self.__depth_level * 3 - 2

        parser_tree = self.__parser.build_tree(inp_root)

        self.__buffer = MatrixBuffer(parser_tree.width + self.__margin_left, height)

        self.__fill_buffer(parser_tree, 1, self.__margin_left)

        buffer = self.__buffer
        del self.__depth_level
        del self.__buffer

        return buffer

    #
    #
    def __fill_buffer(self, node: BinNode, depth: int, margin_global: int):
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
            self.__fill_buffer(node.left, depth + 1, margin_global)

        if node.right is not None:
            self.__fill_dash('right', node.right.key, depth * 3 - 1, margin_key, margin_right)
            self.__fill_buffer(node.right, depth + 1, margin_global_right)

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

    #
    #
    def config(self, struct_node: tuple = None, dash: str = '-', dash_size: int = 3, margin_left: int = 0, float_format: str = '{:.2f}'):
        '''
        Configures settings.
        Args:
            struct_node: Structure information of input node. This is a tuple which comprises 3 elemenets:
                (name_key, name_left_child, name_right_child)
            dash: Dash character. The term "dash" means a horizontal line connecting left and right leaves.
            dash_size: Dash size (the length between left and right leaves).
            margin_left: Left margin of output string result.
            float_format: Format string for displaying floating-point numbers.
        Returns:
            String result.
        '''
        if struct_node is not None:
            if type(struct_node) is not tuple or len(struct_node) != 3:
                raise ValueError('Invalid argument: struct_node must be tuple of 3 elements')

        if type(margin_left) is not int or margin_left < 0:
            raise ValueError('Invalid argument: margin_left must be non-negative integer')

        if type(dash) is not str or len(dash) != 1:
            raise ValueError('Invalid argument: dash must be string of length 1')

        if type(dash_size) is not int or dash_size < 1:
            raise ValueError('Invalid argument: dash_size must be positive integer')

        if type(float_format) is not str:
            raise ValueError('Invalid argument: float_format must be string')

        # Finish arguments validation

        if struct_node is not None:
            self.__parser.config_struct_input_node(struct_node[0], struct_node[1], struct_node[2])

        self.__parser.config_dash(dash, dash_size)

        self.__margin_left = margin_left
        self.__vutil.set_float_format(float_format)
