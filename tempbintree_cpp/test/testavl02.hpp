#ifndef __TEST_AVL_02_HPP__
#define __TEST_AVL_02_HPP__


#include <iostream>
#include <vector>
#include "binarytree/avltree.hpp"

using namespace my::bt;



namespace my
{
namespace testavl02
{



void printTree(AvlTree<int> &avl)
{
    std::vector<int*> res = avl.traverse(OrderTraverse::IN);

    std::cout << "\n print tree: ";

    for (auto &&value : res)
    {
        std::cout << (*value) << "  ";
    }
}



void dotask()
{
    auto avl = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25, 100, 28, 140} )
    {
        std::cout << "\n\n inserts " << value;
        avl.insert(value);
        printTree(avl);
        std::cout << "\n height: " << avl.height();
    }

    std::cout << std::endl;

    for ( auto &&value : {30, 50, 140, 25, 20, 10, 40, 100, 28} )
    {
        std::cout << "\n\n removes " << value;
        avl.remove(value);
        printTree(avl);
        std::cout << "\n height: " << avl.height();
    }


    std::cout << std::endl;
}



} // test
} // my



#endif
