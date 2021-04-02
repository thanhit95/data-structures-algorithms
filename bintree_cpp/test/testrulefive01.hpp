#ifndef __TEST_RULE_OF_FIVE_01_HPP__
#define __TEST_RULE_OF_FIVE_01_HPP__


#include <iostream>
#include <vector>
#include "binarytree/avltree.hpp"
#include "binarytreedisp/display.hpp"

using namespace my::bt;
using namespace my::btdisp;



namespace my
{
namespace testrulefive01
{



void printTree(AvlTree<int> &avl)
{
    auto display = BinTreeDisplay< AvlNode<int> >();

    display.config('-', 1, 0, 2);

    auto res = display.get(avl._getRoot());

    std::cout << res;
}



void dotask()
{
    auto a = AvlTree<int>();

    for ( auto &&value : {10, 20, 30, 40, 50, 25} )
        a.insert(value);


    auto b = a; // copy constructor
    b.insert(60);
    b.insert(12);
    printTree(b);


    std::cout << "\n\n\n";


    auto c = b; // copy constructor
    c = a;      // copy assignment operator
    printTree(c);


    std::cout << std::endl;
}



} // test
} // my




#endif
