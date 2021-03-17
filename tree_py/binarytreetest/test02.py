from binarytree import BinarySearchTree


def dotask():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 8]:
        bst.insert(value)

    print(bst)
    print('min:', bst.min())
    print('max:', bst.max())

    for value in bst:
        print(value, end='  ')