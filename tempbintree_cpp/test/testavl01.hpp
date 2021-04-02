#ifndef __TEST_AVL_01_HPP__
#define __TEST_AVL_01_HPP__


#include <iostream>
#include <vector>
#include "binarytree/avltree.hpp"

using namespace my::bt;



namespace my
{
namespace testavl01
{


void printTree(AvlTree<int> &avl)
{
    std::vector<int*> res = avl.traverse(OrderTraverse::IN);

    std::cout << "\n\n print tree: ";

    for (auto &&value : res)
    {
        std::cout << (*value) << "  ";
    }

    std::cout << std::endl;
}



void dotask()
{
    auto avl = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25} )
        avl.insert(value);

    // std::cout << bst;

    std::cout << "\n\n count: " << avl.count();

    std::cout << "\n\n min: " << avl.getMin();

    std::cout << "\n\n max: " << avl.getMax();

    std::cout << "\n\n contain: " << avl.contain(50);

    std::cout << "\n\n height: " << avl.height();

    printTree(avl);


    std::cout << std::endl;
}



} // test
} // my



#endif
