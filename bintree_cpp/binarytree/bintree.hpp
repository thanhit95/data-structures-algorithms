#ifndef __BIN_TREE_HPP__
#define __BIN_TREE_HPP__


#include <vector>
#include <algorithm>
#include "binnode.hpp"
#include "global.hpp"


namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BinTree
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
protected:
    TNode *root = nullptr;

    std::vector<TKey*> resTraversal;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    inline bool empty() const
    {
        return (nullptr == this->root);
    }



public:
    int height() const
    {
        return __height(root);
    }



public:
    // WARNING: This getter method may cause the tree to malfunction.
    TNode* _getRoot() const
    {
        return this->root;
    }



public:
    std::vector<TKey*> traverse(const TraverseOrder &order)
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



} // bt
} // my


#endif // __BIN_TREE_HPP__
