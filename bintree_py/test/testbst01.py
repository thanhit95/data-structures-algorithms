from binarytree import BinarySearchTree


def dotask():
    bst = BinarySearchTree(candd_removal='right')

    for value in [12, 39, 20, 7, 26, 45, 19, 8]:
        bst.insert(value)

    print(bst)

    print('count:', bst.count())
    print('min:', bst.min())
    print('max:', bst.max())
    print('contain:', bst.contain(20))

    print('tree traveler: ', end='')
    print(bst.traverse(order='in'))

    print('using for each to iterate nodes in tree')

    for value in bst:
        print(value, end='  ')

    print(end='\n')

    _ = bst.remove(800)
    _ = bst.remove(12)

    print(bst)
    print('count:', bst.count())
