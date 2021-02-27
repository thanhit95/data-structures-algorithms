import math
from binnode import BinNode
from bst import BinarySearchTree


class BinTreeDisplay:
    #
    #
    def __init__(self):
        self.__config_str_float_format = '{value:.2f}'

    #
    #
    def __config_dash(self, dash, dash_size):
        if type(dash) is not str or len(dash) != 1:
            raise ValueError('Invalid argument: dash must be string of length 1')

        if type(dash_size) is not int or dash_size < 1:
            raise ValueError('Invalid argument: dash_size must be positive integer')

        self.__config_str_dash = dash
        self.__config_size_horizontal_dash = dash_size

    #
    #
    def get_str(self, bst: BinarySearchTree, dash: str = '-', dash_size: int = 3):
        self.__config_dash(dash, dash_size)

        self.__depth_level = bst.depth_level()

        width, _, _, _, _ = self.__get_width_node(bst.root)
        height = self.__depth_level * 2 - 1

        self.__matrix = BinTreeDisplayMatrix(width, height)

        self.__fill_matrix(bst.root, 1, 0)

        matrix = self.__matrix
        del self.__depth_level
        del self.__matrix

        return matrix.get_str()

    #
    #
    def __get_width_node(self, node: BinNode):
        if node is None:
            return 0, 0, 0, 0, 0

        width_left_branch, _, _, _, _ = self.__get_width_node(node.left)
        width_right_branch, _, _, _, _ = self.__get_width_node(node.right)

        full_dash_size = self.__config_size_horizontal_dash
        len_key = self.__get_len_value(node.key)

        size_left_dash = 0 if node.left is None else full_dash_size // 2
        size_right_dash = 0 if node.right is None else full_dash_size // 2

        full_width = width_left_branch + width_right_branch + size_left_dash + size_right_dash

        size_right_overflow = len_key - (width_right_branch + size_right_dash)
        full_width += max(1, size_right_overflow)

        return full_width, width_left_branch, width_right_branch, size_left_dash, size_right_dash

    #
    #
    def __fill_matrix(self, node: BinNode, depth: int, margin_global: int):
        if node is None:
            return

        _, width_left_branch, _, size_left_dash, size_right_dash = self.__get_width_node(node)
        str_value = self.__get_value_str(node.key)

        margin = margin_global + width_left_branch + size_left_dash

        self.__matrix.fill(margin, depth * 2 - 2, str_value)

        if node.left is not None or node.right is not None:
            self.__matrix.fill(margin, depth * 2 - 1, '|')

        self.__fill_matrix(node.left, depth + 1, margin_global)
        self.__fill_matrix(node.right, depth + 1, margin + 1 + size_right_dash)

        if node.left is not None:
            self.__fill_horizontal_dash(margin, depth * 2, 'left')

        if node.right is not None:
            self.__fill_horizontal_dash(margin, depth * 2, 'right')

    #
    #
    def __fill_horizontal_dash(self, posx, posy, direction):
        matrix = self.__matrix
        a = matrix.a
        dash = self.__config_str_dash

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

            for x in range(posx, matrix.width):
                if a[posy][x] == ' ':
                    a[posy][x] = dash
                else:
                    break

        else:
            raise ValueError('Invalid argument: direction')

    #
    #
    def __get_len_value(self, value):
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
            value_str = self.__get_value_str(value)
            res = len(value_str)
        elif type_value is str:
            res = len(value)
        else:
            res = len(str(value))

        return res

    #
    #
    def __get_value_str(self, value):
        type_value = type(value)

        if type_value is float:
            return self.__config_str_float_format.format(value=value)

        if type_value is str:
            return value

        return str(value)


#
#
class BinTreeDisplayMatrix:
    #
    #
    def __init__(self, width, height):
        self.width = width
        self.height = height

        cell = ' '

        self.a = [[cell] * width for i in range(height)]

    #
    #
    def fill(self, posx: int, posy: int, value: str):
        if posx < 0:
            raise ValueError('Invalid argument: posx')

        if posy >= self.height:
            raise ValueError('Invalid argument: posy')

        if type(value) is not str:
            raise ValueError('Invalid argument: value --> must be string')

        a = self.a
        len_value = len(value)

        for i in range(len_value):
            if posx + i >= self.width:
                break

            a[posy][posx + i] = value[i]

    #
    #
    def get_str(self):
        a = self.a
        lst_rows = [''.join(a[i]).rstrip() for i in range(self.height)]
        res = '\n'.join(lst_rows)
        return res
