'''

BINARY TREE DISPLAY

Description:    A utility help visualize binary trees by using ASCII text.

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


from .parsingnode import ParsingNode
from .valueutil import ValueUtil
from .matrixbuffer import MatrixBuffer
from .displayparser import DisplayParser


#
#
class BinTreeDisplay:
    '''
    Binary tree display. A utility help visualize binary trees by using ASCII text.
    '''
    #
    #
    #################################################################
    #                        METHODS (PUBLIC)
    #################################################################
    #
    #
    def __init__(self):
        self._vutil = ValueUtil()
        self._parser = DisplayParser(self._vutil)
        self._buffer = None
        self._margin_left = 0
        self.config(struct_node=('key', 'left', 'right'))

    #
    #
    def get(self, inp_root) -> str:
        '''
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            struct_node, line_char, line_brsp, margin_left, float_pre
        Args:
            inp_root: Input root of binary search tree.
        Returns:
            String result. If inp_root is None then returns an empty string.
        '''
        if inp_root is None:
            return ''

        self._process(inp_root)
        assert self._buffer is not None

        res = self._buffer.get_str()

        self._buffer = None
        return res

    #
    #
    def get_lst_rows(self, inp_root) -> list:
        '''
        Gets display string for binary search tree.
        Output result can be configured by calling "config" method. Configurable properties are:
            struct_node, line_char, line_brsp, margin_left, float_pre
        Returns:
            List of rows. Each row is a string. If inp_root is None then returns an empty list.
        '''
        if inp_root is None:
            return []

        self._process(inp_root)
        assert self._buffer is not None

        res = self._buffer.get_lst_rows()

        self._buffer = None
        return res

    #
    #
    def config(self, struct_node: tuple = None, line_char: str = '-', line_brsp: int = 1, margin_left: int = 0, float_pre: int = 2):
        '''
        Configures settings.
        Args:
            struct_node: Structure information of input node. This is a tuple which comprises 3 elemenets:
                (name_key, name_left_child, name_right_child)
            line_char: Display character for the horizontal line connecting left-right branches.
            line_brsp: Branch spacing value for the horizontal line connecting left-right branches.
            margin_left: Left margin of output string result.
            float_pre: Maximum precision of floating-point numbers when displays.
        '''
        if struct_node is not None:
            if type(struct_node) is not tuple or len(struct_node) != 3:
                raise ValueError('Invalid argument: struct_node must be a tuple of 3 elements')

        if type(margin_left) is not int or margin_left < 0:
            raise ValueError('Invalid argument: margin_left must be a non-negative integer')

        if type(line_char) is not str or len(line_char) != 1:
            raise ValueError('Invalid argument: line_char must be a string of length 1')

        if type(line_brsp) is not int or line_brsp < 1:
            raise ValueError('Invalid argument: line_brsp must be a positive integer')

        if type(float_pre) is not int or float_pre < 0:
            raise ValueError('Invalid argument: float_pre must be a non-negative integer')

        # Finish arguments validation

        if struct_node is not None:
            self._parser.config_struct_input_node(struct_node[0], struct_node[1], struct_node[2])

        self._parser.config_line(line_char, line_brsp)
        self._vutil.set_float_precision(float_pre)
        self._margin_left = margin_left

    #
    #
    #################################################################
    #                        METHODS (PROTECTED)
    #################################################################
    #
    #
    def _process(self, inp_root):
        '''
        Backend function for "get" method.
        '''
        height_inp_root = self._parser.get_height(inp_root)
        height = height_inp_root * 3 - 2

        parsing_tree = self._parser.build_tree(inp_root)

        self._buffer = MatrixBuffer(parsing_tree.width + self._margin_left, height)

        self._fill_buffer(parsing_tree, 1, self._margin_left)

        self._parser.destroy_tree(parsing_tree)

    #
    #
    def _fill_buffer(self, node: ParsingNode, depth: int, margin_global: int):
        if node is None:
            return

        margin_key = margin_global + node.margin_key
        margin_left = margin_global + node.margin_left_child
        margin_right = margin_global + node.margin_right_child
        margin_global_right = margin_key + 1 + node.size_right_line

        self._buffer.fill(margin_key, depth * 3 - 3, node.key)

        if node.left is not None or node.right is not None:
            self._buffer.fill(margin_key, depth * 3 - 2, '|')

        if node.left is not None:
            self._fill_line('left', node.left.key, depth * 3 - 1, margin_left, margin_key)
            self._fill_buffer(node.left, depth + 1, margin_global)

        if node.right is not None:
            self._fill_line('right', node.right.key, depth * 3 - 1, margin_key, margin_right)
            self._fill_buffer(node.right, depth + 1, margin_global_right)

    #
    #
    def _fill_line(self, direction: str, child_key: str, y: int, margin_a: int, margin_b: int):
        if direction not in ('left', 'right'):
            raise ValueError('Invalid argument: direction')

        if direction == 'left':
            margin_a += len(child_key) - 1

        self._buffer.fill_line(self._parser.line_char, y, margin_a, margin_b)
