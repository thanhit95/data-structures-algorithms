from binnode import BinNode
from bst import BinarySearchTree
from bintreedisplayparser import ValueParserUtil, BinTreeDisplayParser


class BinTreeDisplay:
    #
    #
    def __init__(self):
        self.__putil = ValueParserUtil()
        self.__parser = BinTreeDisplayParser(self.__putil)

    #
    #
    def get_str(self, bst: BinarySearchTree, dash: str = '-', dash_size: int = 3):
        self.__parser.config_dash(dash, dash_size)

        self.__depth_level = bst.depth_level()

        width, _, _, _, _ = self.__parser.get_width_node(bst.root)
        height = self.__depth_level * 2 - 1

        self.__matrix = BinTreeDisplayMatrix(width, height)

        self.__fill_matrix(bst.root, 1, 0)

        matrix = self.__matrix
        del self.__depth_level
        del self.__matrix

        return matrix.get_str()

    #
    #
    def __fill_matrix(self, node: BinNode, depth: int, margin_global: int):
        if node is None:
            return

        _, width_left_branch, _, size_left_dash, size_right_dash = self.__parser.get_width_node(node)
        str_value = self.__putil.get_str(node.key)

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

            for x in range(posx, matrix.width):
                if a[posy][x] == ' ':
                    a[posy][x] = dash
                else:
                    break

        else:
            raise ValueError('Invalid argument: direction')


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
