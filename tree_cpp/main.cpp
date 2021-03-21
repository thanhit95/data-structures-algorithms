#include <iostream>
#include "binarytree/bst.hpp"

using namespace mybt;

int main(int, char**)
{
    std::cout << "Hello tree" << std::endl;

    BinarySearchTree<int> tree;

    tree.insert(50);
    tree.insert(25);
    tree.insert(80);
    tree.insert(10);
    tree.insert(40);
    tree.insert(90);

    std::vector<int*> res = tree.traverse(TraverseOrder::IN);
    std::cout << "counts: " << res.size() << std::endl;

    for (auto &e : res)
    {
        std::cout << *e << std::endl;
    }

    BinNode<int> *getRes = tree.get(40);
    std::cout << "count: " << tree.count() << std::endl;


    std::cout << "\n\nremove key" << std::endl;

    tree.remove(50);

    res = tree.traverse(TraverseOrder::IN);
    std::cout << "count: " << tree.count() << std::endl;

    for (auto &e : res)
    {
        std::cout << *e << std::endl;
    }

    return 0;
}
