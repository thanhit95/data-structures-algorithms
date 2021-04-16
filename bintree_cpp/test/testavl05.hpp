#ifndef __TEST_AVL_05_HPP__
#define __TEST_AVL_05_HPP__


#include <iostream>
#include <string>
#include "testbase.hpp"
#include "binarytree/avltree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace avl05
{



void doTask()
{
    auto avl = AvlTree<char>(CandidateRemoval::RIGHT);

    for ( auto &&value : std::string("INFORMATIONTECHNOLOGY") )
    {
        std::cout << "\n\n\n\n insert " << value << "\n" << std::endl;
        avl.insert(value);
        base::displayTree(avl);
    }

    std::cout << std::endl;


    for ( auto &&value : std::string("ECI") )
    {
        std::cout << "\n\n\n\n remove " << value << "\n" << std::endl;
        avl.remove(value);
        base::displayTree(avl);
    }

    std::cout << std::endl;
}



}
} // test
} // my



#endif
