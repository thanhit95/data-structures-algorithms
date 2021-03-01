import math
from binnode import BinNode


class ValueUtil:
    #
    #
    def __init__(self):
        self.__float_format = '{:.2f}'

    #
    #
    def get_float_format(self):
        return self.__float_format

    #
    #
    def set_float_format(self, fmt: str):
        if type(fmt) is not str:
            raise ValueError('Invalid argument: fmt must be string')

        self.__float_format = fmt

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
            return self.__float_format.format(value)

        if type_value is str:
            return value

        return str(value)


#
#
class BinTreeDisplayParser:
    #
    #
    def __init__(self, value_util: ValueUtil, dash: str = '-', dash_size: int = 3):
        self.__vutil = value_util
        self.config_struct_input_node('key', 'left', 'right')
        self.config_dash(dash, dash_size)

    #
    #
    def config_struct_input_node(self, key: str, left_child: str, right_child: str):
        '''
        Configures input node structure for flexibility.
        Args:
            key: Name of key.
            left_child: Name of left child.
            right_child: Name of right child.
        '''
        if key is None or type(key) is not str:
            raise ValueError('Invalid argument: key must be string')

        if left_child is None or type(left_child) is not str:
            raise ValueError('Invalid argument: left_child must be string')

        if right_child is None or type(right_child) is not str:
            raise ValueError('Invalid argument: right_child must be string')

        self.struct_node_key = key
        self.struct_node_le = left_child
        self.struct_node_ri = right_child

    #
    #
    def config_dash(self, dash, dash_size):
        '''
        Configures dash information. The term "dash" means a horizontal line connecting left and right leaves.
        Args:
            dash: Dash character.
            dash_size: Dash size (the length between left and right leaves).
        '''
        if type(dash) is not str or len(dash) != 1:
            raise ValueError('Invalid argument: dash must be string of length 1')

        if type(dash_size) is not int or dash_size < 1:
            raise ValueError('Invalid argument: dash_size must be positive integer')

        self.dash = dash
        self.dash_size = dash_size

    #
    #
    def build_tree(self, input_root):
        '''
        Builds parser tree which stores parsing information of each corresponding node.
        The structure of input_root (and its nodes) should be configured by function config_struct_input_node.
        Args:
            input_root: Input root node.
        Returns:
            A node of type BinNode indicating parser tree.
        '''
        if input_root is None:
            return None

        input_key = getattr(input_root, self.struct_node_key)
        input_left = getattr(input_root, self.struct_node_le)
        input_right = getattr(input_root, self.struct_node_ri)

        node = BinNode(self.__vutil.get_str(input_key))
        len_key = len(node.key)

        node.left = self.build_tree(input_left)
        node.right = self.build_tree(input_right)

        width_left_branch = 0 if node.left is None else node.left.width
        width_right_branch = 0 if node.right is None else node.right.width

        size_left_dash = 0 if node.left is None else self.dash_size // 2
        size_right_dash = 0 if node.right is None else self.dash_size // 2

        full_width = width_left_branch + width_right_branch + size_left_dash + size_right_dash

        size_right_overflow = len_key - (width_right_branch + size_right_dash)
        full_width += max(1, size_right_overflow)

        margin_key = width_left_branch + size_left_dash
        margin_left_child = 0 if node.left is None else node.left.margin_key
        margin_right_child = 0 if node.right is None else margin_key + node.right.margin_key + size_right_dash + 1

        node.width = full_width
        node.width_left_branch = width_left_branch
        node.width_right_branch = width_right_branch
        node.size_left_dash = size_left_dash
        node.size_right_dash = size_right_dash

        node.margin_key = margin_key
        node.margin_left_child = margin_left_child
        node.margin_right_child = margin_right_child

        return node

    #
    #
    def get_depth_level(self, node):
        '''
        Gets depth level of the tree.
        Args:
            node: Input root of the tree.
        Returns:
            Depth level.
        '''
        if node is None:
            return 0

        node_left = getattr(node, self.struct_node_le)
        node_right = getattr(node, self.struct_node_ri)

        depth_left_branch = 1 + self.get_depth_level(node_left)
        depth_right_branch = 1 + self.get_depth_level(node_right)

        return max(depth_left_branch, depth_right_branch)
