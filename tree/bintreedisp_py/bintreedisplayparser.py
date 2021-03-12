import math
from binnode import BinNode


class ValueUtil:
    #
    #
    def __init__(self):
        self.__float_precision = 2

    #
    #
    def get_float_precision(self):
        return self.__float_precision

    #
    #
    def set_float_precision(self, precision: int):
        if type(precision) is not int or precision < 1:
            raise ValueError('Invalid argument: precision must be positive integer')

        self.__float_precision = precision

    #
    #
    def get_str(self, value):
        type_value = type(value)

        if type_value is float:
            return str(round(value, self.__float_precision))

        if type_value is str:
            return value

        return str(value)


#
#
class BinTreeDisplayParser:
    #
    #
    def __init__(self, value_util: ValueUtil, character: str = '-', branch_space: int = 3):
        self.__vutil = value_util
        self.config_struct_input_node('key', 'left', 'right')
        self.config_line(character, branch_space)

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
    def config_line(self, character, branch_spacing):
        '''
        Configures line information. The term "line" means a horizontal line connecting left-right branches.
        Args:
            character: Display character.
            branch_spacing: Branch spacing.
        '''
        if type(character) is not str or len(character) != 1:
            raise ValueError('Invalid argument: character must be string of length 1')

        if type(branch_spacing) is not int or branch_spacing < 1:
            raise ValueError('Invalid argument: branch_spacing must be positive integer')

        self.line_char = character
        self.line_brsp = branch_spacing

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

        size_left_line = 0 if node.left is None else self.line_brsp
        size_right_line = 0 if node.right is None else self.line_brsp

        full_width = width_left_branch + width_right_branch + size_left_line + size_right_line

        size_right_overflow = len_key - (width_right_branch + size_right_line)
        full_width += max(1, size_right_overflow)

        margin_key = width_left_branch + size_left_line
        margin_left_child = 0 if node.left is None else node.left.margin_key
        margin_right_child = 0 if node.right is None else margin_key + node.right.margin_key + size_right_line + 1

        node.width = full_width
        node.width_left_branch = width_left_branch
        node.width_right_branch = width_right_branch
        node.size_left_line = size_left_line
        node.size_right_line = size_right_line

        node.margin_key = margin_key
        node.margin_left_child = margin_left_child
        node.margin_right_child = margin_right_child

        return node

    #
    #
    def get_height(self, node):
        '''
        Gets height of the tree.
        Args:
            node: Input root of the tree.
        Returns:
            Height.
        '''
        if node is None:
            return 0

        node_left = getattr(node, self.struct_node_le)
        node_right = getattr(node, self.struct_node_ri)

        height_le_branch = 1 + self.get_height(node_left)
        height_ri_branch = 1 + self.get_height(node_right)

        return max(height_le_branch, height_ri_branch)
