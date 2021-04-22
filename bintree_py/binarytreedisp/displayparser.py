from .parsingnode import ParsingNode
from .valueutil import ValueUtil


#
#
class DisplayParser:
    #
    #
    def __init__(self, value_util: ValueUtil, character: str = '-', branch_spacing: int = 1):
        if value_util is None:
            raise ValueError('value_util cannot be None')

        self.value_util = value_util
        self.config_struct_input_node('key', 'left', 'right')
        self.config_line(character, branch_spacing)

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
            raise ValueError('Invalid argument: key must be a string')

        if left_child is None or type(left_child) is not str:
            raise ValueError('Invalid argument: left_child must be a string')

        if right_child is None or type(right_child) is not str:
            raise ValueError('Invalid argument: right_child must be a string')

        self.struct_node_key = key
        self.struct_node_le = left_child
        self.struct_node_ri = right_child

    #
    #
    def config_line(self, character: str, branch_spacing: int):
        '''
        Configures line information. The term "line" means a horizontal line connecting left-right branches.
        Args:
            character: Display character.
            branch_spacing: Branch spacing.
        '''
        if type(character) is not str or len(character) != 1:
            raise ValueError('Invalid argument: character must be a string of length 1')

        if type(branch_spacing) is not int or branch_spacing < 1:
            raise ValueError('Invalid argument: branch_spacing must be a positive integer')

        self.line_char = character
        self.line_brsp = branch_spacing

    #
    #
    def build_tree(self, input_root) -> ParsingNode:
        '''
        Builds parser tree which stores parsing information of each corresponding node.
        The structure of input_root (and its nodes) should be configured by function config_struct_input_node.
        Args:
            input_root: Input root node.
        Returns:
            A node of type ParsingNode indicating parsing tree.
        '''
        if input_root is None:
            return None

        input_key = getattr(input_root, self.struct_node_key)
        input_left = getattr(input_root, self.struct_node_le)
        input_right = getattr(input_root, self.struct_node_ri)

        node = ParsingNode(self.value_util.get_str(input_key))
        len_key = len(node.key)

        node.left = self.build_tree(input_left)
        node.right = self.build_tree(input_right)

        node_left_none = node.left is None
        node_right_none = node.right is None

        width_left_branch = 0 if node_left_none else node.left.width
        width_right_branch = 0 if node_right_none else node.right.width

        size_left_line = 0 if node_left_none else self.line_brsp
        size_right_line = 0 if node_right_none else self.line_brsp

        full_width = width_left_branch + width_right_branch + size_left_line + size_right_line

        size_right_overflow = len_key - (width_right_branch + size_right_line)
        full_width += max(1, size_right_overflow)

        margin_key = width_left_branch + size_left_line
        margin_left_child = 0 if node_left_none else node.left.margin_key
        margin_right_child = 0 if node_right_none else margin_key + node.right.margin_key + size_right_line + 1

        node.width = full_width
        node.width_left_branch = width_left_branch
        node.width_right_branch = width_right_branch
        node.size_left_line = size_left_line
        node.size_right_line = size_right_line

        node.margin_key = margin_key
        node.margin_left_child = margin_left_child
        node.margin_right_child = margin_right_child

        del input_key
        del input_left
        del input_right
        del len_key
        del node_left_none
        del node_right_none
        del width_left_branch
        del width_right_branch
        del size_left_line
        del size_right_line
        del full_width
        del size_right_overflow
        del margin_key
        del margin_left_child
        del margin_right_child

        return node

    #
    #
    def destroy_tree(self, node: ParsingNode):
        if node is None:
            return

        self.destroy_tree(node.left)
        del node.left

        self.destroy_tree(node.right)
        del node.right

        del node.key

    #
    #
    def get_height(self, node) -> int:
        if node is None:
            return 0

        height_le = self.get_height(getattr(node, self.struct_node_le))
        height_ri = self.get_height(getattr(node, self.struct_node_ri))

        return 1 + max(height_le, height_ri)
