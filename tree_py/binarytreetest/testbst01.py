from binarytree import BinarySearchTree


def dotask():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print(bst)

    print('count:', bst.count())
    print('min:', bst.min())
    print('max:', bst.max())
    print('get key:', bst.get(20))

    print('Using for each to iterate nodes in tree')

    for value in bst:
        print(value, end='  ')

    print(end='\n')

    _ = bst.remove(800)
    _ = bst.remove(12)

    print(bst)
    print('count:', bst.count())
