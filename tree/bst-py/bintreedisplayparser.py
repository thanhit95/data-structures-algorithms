import math
from binnode import BinNode
from bst import BinarySearchTree


#
#
class ValueParserUtil:
    #
    #
    def __init__(self):
        self.float_format = '{value:.2f}'

    #
    #
    def get_len(self, value):
        type_value = type(value)
        res = 0

        if type_value is int:
            if value > 0:
                res = int(math.log10(value)) + 1
            elif value == 0:
                res = 1
            else:
                res = int(math.log10(-value)) + 2
        elif type_value is float:
            value_str = self.get_str(value)
            res = len(value_str)
        elif type_value is str:
            res = len(value)
        else:
            res = len(str(value))

        return res

    #
    #
    def get_str(self, value):
        type_value = type(value)

        if type_value is float:
            return self.float_format.format(value=value)

        if type_value is str:
            return value

        return str(value)


#
#
class BinTreeDisplayParser:
    #
    #
    def __init__(self, parser_util: ValueParserUtil, dash: str = '-', dash_size: int = 3):
        self.__util = parser_util
        self.config_dash(dash, dash_size)

    #
    #
    def config_dash(self, dash, dash_size):
        if type(dash) is not str or len(dash) != 1:
            raise ValueError('Invalid argument: dash must be string of length 1')

        if type(dash_size) is not int or dash_size < 1:
            raise ValueError('Invalid argument: dash_size must be positive integer')

        self.dash = dash
        self.dash_size = dash_size

    #
    #
    def get_width_node(self, node: BinNode):
        return self.__get_width_node(node)

    #
    #
    def __get_width_node(self, node: BinNode):
        if node is None:
            return 0, 0, 0, 0, 0

        width_left_branch, _, _, _, _ = self.__get_width_node(node.left)
        width_right_branch, _, _, _, _ = self.__get_width_node(node.right)

        full_dash_size = self.dash_size
        len_key = self.__util.get_len(node.key)

        size_left_dash = 0 if node.left is None else full_dash_size // 2
        size_right_dash = 0 if node.right is None else full_dash_size // 2

        full_width = width_left_branch + width_right_branch + size_left_dash + size_right_dash

        size_right_overflow = len_key - (width_right_branch + size_right_dash)
        full_width += max(1, size_right_overflow)

        return full_width, width_left_branch, width_right_branch, size_left_dash, size_right_dash
