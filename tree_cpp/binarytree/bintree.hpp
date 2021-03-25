#ifndef __BIN_TREE_HPP__
#define __BIN_TREE_HPP__


#include <vector>
#include <algorithm>
#include "binnode.hpp"
#include "global.hpp"


namespace mybt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BinTree
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
public:
    TNode *root = nullptr;

    std::vector<TKey*> resTraversal;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    std::vector<TKey*> traverse(TraverseOrder order)
    {
        resTraversal.clear();

        switch (order)
        {
        case TraverseOrder::PRE :
            traversePre(root);
            break;

        case TraverseOrder::IN :
            traverseIn(root);
            break;

        case TraverseOrder::POST :
            traversePost(root);
            break;

        default:
            break;
        }

        return resTraversal;
    }



public:
    int const height() const
    {
        return __height(root);
    }



protected:
    void traversePre(TNode *node)
    {
        if (nullptr == node)
            return;

        resTraversal.push_back(&node->key);
        traversePre(node->left);
        traversePre(node->right);
    }


    void traverseIn(TNode *node)
    {
        if (nullptr == node)
            return;

        traverseIn(node->left);
        resTraversal.push_back(&node->key);
        traverseIn(node->right);
    }


    void traversePost(TNode *node)
    {
        if (nullptr == node)
            return;

        traversePost(node->left);
        traversePost(node->right);
        resTraversal.push_back(&node->key);
    }



    int __height(TNode *node) const
    {
        if (nullptr == node)
            return 0;

        int heightLe = 1 + __height(node->left);
        int heightRi = 1 + __height(node->right);

        return std::max(heightLe, heightRi);
    }
};



} // mybt


#endif
