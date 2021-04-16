#ifndef __TEST_RULE_OF_FIVE_01_HPP__
#define __TEST_RULE_OF_FIVE_01_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/avltree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace rulefive01
{



void doTask()
{
    auto a = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25} )
        a.insert(value);


    auto b = a; // copy constructor
    b.insert(60);
    b.insert(12);
    base::displayTree(b);


    std::cout << "\n\n\n";


    auto c = AvlTree<int>();
    c = a;      // copy assignment operator
    base::displayTree(c);


    std::cout << std::endl;
}



}
} // test
} // my



#endif
