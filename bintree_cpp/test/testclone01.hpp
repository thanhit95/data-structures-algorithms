#ifndef __TEST_CLONE_01_HPP__
#define __TEST_CLONE_01_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/avltree.hpp"

using namespace my::bt;



namespace my
{
namespace test
{
namespace clone01
{



void doTask()
{
    auto a = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25, 100, 28, 140} )
        a.insert(value);


    std::cout << " display tree a:" << std::endl;
    base::displayTree(a);


    auto b = a;
    std::cout << "\n\n\n display tree b:" << std::endl;
    base::displayTree(b);
    std::cout << "\n\n height tree b: " << b.height() << std::endl;


    auto c = a;
    c.clear();
    std::cout << "\n\n\n display tree c:" << std::endl;
    base::displayTree(c);


    std::cout << std::endl;
}



}
} // test
} // my



#endif
