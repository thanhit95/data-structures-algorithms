#include <iostream>
#include "binarytree/bst.hpp"

using namespace mybt;

int main(int, char**)
{
    std::cout << "Hello tree" << std::endl;

    BinarySearchTree<int> tree;

    BinNode<> *a = new BinNode<>(50);
    BinNode<> *b = new BinNode<>(25);
    BinNode<> *c = new BinNode<>(80);
    BinNode<> *d = new BinNode<>(10);
    BinNode<> *e = new BinNode<>(40);
    BinNode<> *f = new BinNode<>(90);

    a->left = b;
    a->right = c;
    b->left = d;
    b->right = e;
    c->right = f;

    tree.root = a;

    auto res = tree.traverse(TraverseOrder::IN);

    for (auto &e : res)
    {
        std::cout << *e << std::endl;
    }

    BinNode<int> *getRes = tree.get(40);

    std::cout << "get res: " << getRes->key << std::endl;

    return 0;
}
