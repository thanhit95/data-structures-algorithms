#ifndef __TEST_TRAVERSAL_01_HPP__
#define __TEST_TRAVERSAL_01_HPP__


#include <iostream>
#include "testbase.hpp"
#include "binarytree/binsearchtree.hpp"

using namespace my::test;
using namespace my::bt;



namespace my
{
namespace test
{
namespace traversal01
{



void printList(const std::vector<int> lst)
{
    for ( auto &&value : lst)
    {
        std::cout << value << "  ";
    }

    std::cout << std::endl;
}



void doTask()
{
    auto bst = BinSearchTree<int>();

    for ( auto &&value : {12, 39, 20, 7, 26, 45, 19, 8} )
        bst.insert(value);


    std::cout << "\n display tree:" << std::endl;
    base::displayTree(bst);


    std::cout << "\n\n in-order traversal:" << std::endl;
    printList(bst.traverse(OrderTraversal::IN));

    std::cout << "\n\n pre-order traversal:" << std::endl;
    printList(bst.traverse(OrderTraversal::PRE));

    std::cout << "\n\n post-order traversal:" << std::endl;
    printList(bst.traverse(OrderTraversal::POST));


    std::cout << std::endl;
}



}
} // test
} // my



#endif
