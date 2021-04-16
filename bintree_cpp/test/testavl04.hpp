#ifndef __TEST_AVL_04_HPP__
#define __TEST_AVL_04_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/avltree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace avl04
{



void doTask()
{
    auto avl = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25, 100, 28, 140} )
    {
        std::cout << "\n\n\n insert " << value << std::endl;
        avl.insert(value);
        base::displayTree(avl);
    }

    std::cout << std::endl;


    for ( auto &&value : {30, 50, 140, 25, 20, 10, 40, 100, 28} )
    {
        std::cout << "\n\n\n remove " << value << std::endl;
        avl.remove(value);
        base::displayTree(avl);
    }

    std::cout << std::endl;
}



}
} // test
} // my



#endif
