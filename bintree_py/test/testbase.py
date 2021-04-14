from binarytreedisp import BinTreeDisplay


#
#
def print_tree(tree, order: str = 'in'):
    # print(tree)
    res = tree.traverse(order)
    print(res)


#
#
def display_tree(tree):
    disp = BinTreeDisplay()

    disp.config(struct_node=('key', 'left', 'right'), line_char='-', line_brsp=1, margin_left=0, float_pre=2)

    res = tree.display(disp)
    print(res)

    del disp
